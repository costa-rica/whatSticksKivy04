#kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
#custom
import utils
from utils import CanvasWidget
#python
import json
import requests

Builder.load_file('ps2.kv')

class NavMenu(BoxLayout):...
class Toolbar(MDToolbar):...

class ParentScreen2(Screen):
  email=StringProperty('')
  username=StringProperty('')
  user_timezone=StringProperty('')
  child_sm=ObjectProperty(None)
  def __init__(self,**kwargs):
    super(ParentScreen2,self).__init__(**kwargs)
    print('ParentScreen2 __init__')

  def on_enter(self):
    print('ParentScreen2 on_enter')


  # def toggle_nav_bar(self):
  #   if self.nav_drawer.state=='close':
  #     self.nav_drawer.set_state("open")
  #   else:
  #     self.nav_drawer.set_state("close")

class SuperBox(BoxLayout):...

class ActivityScreen(Screen):
  email=StringProperty('')
  username=StringProperty('')
  user_timezone=StringProperty('')
  def __init__(self,**kwargs):
    super(ActivityScreen,self).__init__(**kwargs)


class TableScreen(Screen):
  def __init__(self,**kwargs):
    super(TableScreen, self).__init__(**kwargs)
