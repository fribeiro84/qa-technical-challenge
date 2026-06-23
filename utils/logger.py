import logging
import os


def configurar_logger(nome, log_file):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(nome)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger