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
Builder.load_file('parentscreen2/ps2.kv')

class NavMenu(BoxLayout):...
class Toolbar(MDToolbar):...

class ParentScreen2(Screen):
  email=StringProperty('')
  username=StringProperty('')
  user_timezone=StringProperty('')
  child_sm=ObjectProperty(None)
  act_screen_id=ObjectProperty(None)
  toolbar=ObjectProperty(None)

  def __init__(self,**kwargs):
    super(ParentScreen2,self).__init__(**kwargs)
    print('ParentScreen2 __init__')

  def on_enter(self):
    print('parentScreen2 on_enter')
    print('self.act_screen_id::', self.act_screen_id)
    self.act_screen_id.user_timezone=self.user_timezone
    self.act_screen_id.date_time_now=current_time_util(self.user_timezone)
    self.act_screen_id.box_layout_date.date_input.text=self.act_screen_id.date_time_now[0]
    self.act_screen_id.box_layout_time.time_input.text=self.act_screen_id.date_time_now[1]


class TableScreen(Screen):
  def __init__(self,**kwargs):
    super(TableScreen, self).__init__(**kwargs)
