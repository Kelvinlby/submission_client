
from . import send_message


async def start_job(name):
    buff = {name: 0.0}
    command = 0
    await send_message(buff, command)
