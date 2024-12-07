import logging
import asyncio
import queue
import threading
from typing import NamedTuple

import grpc
from . import server_pb2
from . import server_pb2_grpc


class UniversalMessage(NamedTuple):
    command: int
    name: str
    value: float

class ClientMessanger:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.message_queue = queue.Queue()
        self.worker_thread = None
        self._stop_event = threading.Event()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                cls._instance = cls()
                cls._instance._start_worker()

        return cls._instance

    def _start_worker(self):
        if self.worker_thread is None:
            self.worker_thread = threading.Thread(target=self._worker_loop)
            self.worker_thread.deamon = True
            self.worker_thread.start()

    def _worker_loop(self):
        while not self._stop_event.is_set():
            try:
                message = self.message_queue.get(timeout=1)
                asyncio.run(self._send_message(message))
                self.message_queue.task_done()
            except queue.Empty:
                self.stop()
                continue
            except Exception as e:
                raise e



    def stop(self):
        self._stop_event.set()
        if self.worker_thread is not None:
            self.worker_thread = None

    @ staticmethod
    async def _send_message(input_message: UniversalMessage):
        """message should be(command: int, name: str, value: float)"""
        command = int(input_message.command)
        name = str(input_message.name)
        value = float(input_message.value)

        async with grpc.aio.insecure_channel("localhost:50051") as channel:
            stub = server_pb2_grpc.ListenerStub(channel)
            logging.info('starting to send message')

            try:
                async def messanger():
                    message = server_pb2.MessageData(
                        command=command,
                        name=name,
                        value=value
                    )
                    logging.info(f'Sending Message: command = {command}, name = {name}, value = {value}')
                    yield message
                    await asyncio.sleep(0.01)

                response = await stub.ListenStream(messanger())
                logging.info(f"Response received: {response.ret}")

            except grpc.RpcError as rpc_error:
                logging.error(f"Error sending message: {rpc_error}")