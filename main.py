from kivymd.app import MDApp
from kivy.lang import Builder
from parentscreen1.ps1 import ParentScreen1
from parentscreen2.ps2 import ParentScreen2
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ColorProperty, StringProperty




# class MainScreenManager(ScreenManager):
#   # parent_screen_1=ObjectProperty(None)
#   def __init__(self,**kwargs):
#     super().__init__(**kwargs)
#     ps1=ParentScreen1()
#     ps2=ParentScreen2()
#     self.add_widget(ps1)
#     self.add_widget(ps2)

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('main_design.kv')

MainApp().run()
