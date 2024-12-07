from .messanger import ClientMessanger, UniversalMessage


def log_metric(name: str, value: float):
    logger = ClientMessanger.get_instance()
    logger.message_queue.put(UniversalMessage(name=name, value=value, command=0))

def start_job(name: str):
    logger = ClientMessanger.get_instance()
    logger.message_queue.put(UniversalMessage(name=name, value=-1.0, command=1))

def end_job(name: str):
    logger = ClientMessanger.get_instance()
    logger.message_queue.put(UniversalMessage(name=name, value=1.0, command=1))

def log_job(name: str, value: float):
    logger = ClientMessanger.get_instance()
    logger.message_queue.put(UniversalMessage(name=name, value=value, command=1))

