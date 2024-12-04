import asyncio
import threading
from .send_message import _send_message


async def __start_job_runner(name: str):
    await _send_message(1, name, -1.0)

def __start_job(name: str):
    asyncio.run(__start_job_runner(name))


def start_job(name: str):
    thread = threading.Thread(target=__start_job, args=(name,))
    thread.daemon = True
    thread.start()