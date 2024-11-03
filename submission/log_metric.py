
from . import send_message


async def log_metric(name, value):
    buff = {name: value}
    command = 0
    await send_message(buff, command)


