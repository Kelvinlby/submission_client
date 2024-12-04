import asyncio
import threading
from .send_message import _send_message


async def __log_job_runner(name: str, value: float):
    await _send_message(1, name, value)

def __log_job(name: str, value: float):
    asyncio.run(__log_job_runner(name, value))


def log_job(name: str, value: float):
    thread = threading.Thread(target=__log_job_runner, args=(name, value))
    thread.daemon = True
    thread.start()