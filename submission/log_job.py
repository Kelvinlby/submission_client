
from . import send_message


async def log_job(name, value):
    buff = {name: value}
    command = 1
    await send_message(buff, command)