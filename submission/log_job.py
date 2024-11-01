
import send_message


def log_job(name, value):
    buff = {name: value}
    command = 1
    send_message.send_message(buff, command)