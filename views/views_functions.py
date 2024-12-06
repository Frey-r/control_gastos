from util import logger_config
from controller import database_controller
from kivymd.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
import datetime


logger = logger_config.get_logger(__name__)
Builder.load_file("views/menu.kv")

class UI(ScreenManager):
    pass

class App(MDApp):
    def prin_data(self, data):
        logger.info(msg=data)
        print(data)

    def send_new_compra(self,precio, cantidad, nombre, distribuidor):
        logger.info("Creando nueva compra")
        compra = {
            'fecha': datetime.datetime.now(),
            'producto_id': "",
            'cantidad': cantidad,
            'proveedor_id': "",
            'marca_id': "",
            'precio': precio
        }
        database_controller.insert_transaccion(compra)
        self.root.current = "menu_principal"
        
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "Lime"
        return UI()
