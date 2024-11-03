
from . import send_message


async def end_job(name):
    buff = {name: 1.0}
    command = 1
    await send_message(buff, command)