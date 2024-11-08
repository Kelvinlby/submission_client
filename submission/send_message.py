import logging
import asyncio
import grpc

from . import server_pb2
from . import server_pb2_grpc



async def send_message(buff, command):
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = server_pb2_grpc.ListenerStub(channel)
        logging.info('starting to send message')

        try:
            async def message_iterator():
                for k, v in buff.items():
                    message = server_pb2.MessageData(
                            command=command,
                            name=k,
                            value=float(v)
                    )
                    logging.info(f'Sending Message: {k} = {v}')
                    yield message
                    await asyncio.sleep(0.01)

            response = await stub.ListenStream(message_iterator())
            logging.info(f"Response received: {response.ret}")

        except grpc.RpcError as rpc_error:
            logging.error(f"Error sending message: {rpc_error}")
