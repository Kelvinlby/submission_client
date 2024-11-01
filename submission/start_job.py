
import send_message


def start_job(name):
    buff = {name: 0.0}
    command = 0
    send_message.send_message(buff, command)
