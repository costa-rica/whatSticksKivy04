from kivymd.app import MDApp
from kivy.lang import Builder
from parentscreen1.ps1 import ParentScreen1
from parentscreen2.ps2 import ParentScreen2
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.metrics import dp
from kivy.core.window import Window
import os;import platform
from screenmodel import CentralData


print('platform.system::',platform.system())
#Darwin
print('os.name:::',os.name)
#posix

if platform in ['ios','android']:
  print('kivy.utils.platform:::', platform)
else:
  Window.size = (640, 1136)#iphone demensions

class MainApp(MDApp):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.central_data = CentralData()

  def build(self):
    return Builder.load_file('main_design.kv')

MainApp().run()
