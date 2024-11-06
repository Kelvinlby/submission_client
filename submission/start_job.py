import asyncio
from .send_message import _send_message


async def __start_job_runner(name: str):
    await _send_message(1, name, -1.0)


def start_job(name: str):
    asyncio.run(__start_job_runner(name))
