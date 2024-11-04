import asyncio
from . import send_message


async def startjob(name):
    buff = {name: 0.0}
    command = 0
    await send_message(buff, command)

def start_job(name):
    asyncio.run(startjob(name))
