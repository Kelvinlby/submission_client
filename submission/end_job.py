
from . import send_message


def end_job(name):
    buff = {name: 1.0}
    command = 1
    send_message(buff, command)