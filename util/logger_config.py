import logging
import datetime
import os

if not os.path.exists("./logs"):
    os.makedirs("./logs")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"./logs/control_gastos_{datetime.datetime.now().strftime('%Y-%m-%d')}.log"),
        #logging.StreamHandler()
    ],
    encoding='utf-8'
)

def get_logger(name = __name__):
    return logging.getLogger(name)

if __name__=='__name__':
    get_logger()

