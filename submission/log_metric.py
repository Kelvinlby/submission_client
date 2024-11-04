import asyncio
from . import send_message


async def logmetric(name, value):
    buff = {name: value}
    command = 0
    await send_message(buff, command)

def log_metric(name, value):
    asyncio.run(logmetric(name, value))
