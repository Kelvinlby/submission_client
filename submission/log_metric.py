import asyncio
from .send_message import _send_message


async def __log_metric_runner(name: str, value: float):
    await _send_message(0, name, float(value))


def log_metric(name: str, value: float):
    asyncio.run(__log_metric_runner(name, value))
