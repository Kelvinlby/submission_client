import asyncio
import threading
from .send_message import _send_message


async def __end_job_runner(name: str):
    await _send_message(1, name, 1.0)

def __end_job(name: str):
    asyncio.run(__end_job_runner(name))


def end_job(name: str):
    thread = threading.Thread(target=__end_job, args=(name,))
    thread.deamon = True
    thread.start()