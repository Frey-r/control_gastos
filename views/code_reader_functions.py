from controller import barcode_controller
from util import logger_config
from kivymd.uix.screenmanager import ScreenManager

logger = logger_config.get_logger(__name__)

class window_code_reader(ScreenManager):
    pass

def read_barcode(self):
    """
        Función que se encarga de leer el código de barras
        Args:
            self (object): objeto de la clase window_code_reader
        Returns:
            None 
    """
    logger.info("Iniciando la lectura del código de barras")