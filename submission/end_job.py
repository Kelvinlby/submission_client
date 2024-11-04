import asyncio
from . import send_message


async def endjob(name):
    buff = {name: 1.0}
    command = 1
    await send_message(buff, command)

def end_job(name):
    asyncio.run(endjob(name))
