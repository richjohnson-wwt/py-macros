
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def get_app_logger(name):
    return logging.getLogger(name)