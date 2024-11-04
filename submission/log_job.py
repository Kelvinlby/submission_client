import asyncio
from . import send_message


async def logjob(name, value):
    buff = {name: value}
    command = 1
    await send_message(buff, command)

def log_job(name, value):
    asyncio.run(logjob(name, value))
