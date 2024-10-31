import logging
import asyncio
import grpc

import server_pb2
import server_pb2_grpc



async def send_message(buff):
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = server_pb2_grpc.ListenerStub(channel)
        logging.info('starting to send message')

        try:
            async def message_iterator():
                for k, v in buff.items():
                    message = server_pb2.MessageData(
                            command=0,
                            name=k,
                            value=float(v)  # Ensure value is float
                    )
                    logging.info(f'Sending Message: {k} = {v}')
                    yield message
                    await asyncio.sleep(0.01)  # Add small delay between messages

            response = await stub.ListenStream(message_iterator())
            logging.info(f"Response received: {response.ret}")

        except grpc.RpcError as rpc_error:
            logging.error(f"Error sending message: {rpc_error}")
