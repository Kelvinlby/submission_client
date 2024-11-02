
from . import send_message


def log_metric(name, value):
    buff = {name: value}
    command = 0
    send_message(buff, command)


