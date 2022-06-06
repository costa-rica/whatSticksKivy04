from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
#custom
import utils
from utils import CanvasWidget, current_time_util
#python
# import json
# import requests
import activityscreen.act_screen
# from myscreen.my_screen import MyScreen
from kivymd.app import MDApp
Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...
class Toolbar(MDToolbar):...

class ParentScreen2(Screen):
  email=StringProperty('')
  username=StringProperty('')
  user_timezone=StringProperty('')
  canvas_widget=ObjectProperty()
  md_nav_layout=ObjectProperty()
  toolbar=ObjectProperty(None)
  child_sm=ObjectProperty(None)
  act_screen_id=ObjectProperty(None)


  def __init__(self,**kwargs):
    super(ParentScreen2,self).__init__(**kwargs)
    print('ParentScreen2 __init__')


  def on_enter(self):
    print('parentScreen2 on_enter')
    myscreen = MDApp.get_running_app().myscreen

    #Things needed to be set by ParentScreen2
    #set height of toolbar
    self.toolbar.height = self.height * .07

    myscreen.toolbar_height = self.toolbar.height
    myscreen.act_screen_height = self.height - self.toolbar.height

    print('***act_screen_height set, now configuring act_screen in my_screen***')
    myscreen.send_to_act_screen(self.act_screen_id)


class TableScreen(Screen):
  def __init__(self,**kwargs):
    super(TableScreen, self).__init__(**kwargs)
