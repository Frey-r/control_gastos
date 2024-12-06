from util import logger_config
from kivymd.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder

logger = logger_config.get_logger(__name__)

class UI(ScreenManager):
    pass

class App(MDApp):
    def working(self):
        print("working")
        logger.info("working")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "Lime"
        Builder.load_file("views/menu.kv")
        return UI()

    