import logging
import asyncio
import grpc
from . import server_pb2
from . import server_pb2_grpc


async def _send_message(command: int, name: str, value):
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = server_pb2_grpc.ListenerStub(channel)
        logging.info('starting to send message')

        try:
            async def messager():
                message = server_pb2.MessageData(
                    command=command,
                    name=name,
                    value=value
                )
                logging.info(f'Sending Message: command = {command}, name = {name}, value = {value}')
                yield message
                await asyncio.sleep(0.01)

            response = await stub.ListenStream(messager())
            logging.info(f"Response received: {response.ret}")

        except grpc.RpcError as rpc_error:
            logging.error(f"Error sending message: {rpc_error}")
