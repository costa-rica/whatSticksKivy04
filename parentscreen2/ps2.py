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
    #Things to pass to act screen
    #user_timezone
    self.act_screen_id.user_timezone=self.user_timezone
    #username
    self.act_screen_id.username=self.username
    #email
    self.act_screen_id.email=self.email

    #set height of toolbar
    self.toolbar.height = self.height * .07

    #create varaible for act_screen_height
    self.act_screen_height = self.height - self.toolbar.height
    #create varaible for width
    print('padding width:::', self.width *.01)
    print('Padding height:::', self.act_screen_height *.01)

    #set height of act_screen
    self.act_screen_id.box_act_screen.height = self.act_screen_height

    #set extra boxlayout height at half of act screen height
    self.act_screen_id.box_act_extra.height = self.act_screen_height *.25

    #set name boxlayout stuff
    self.act_screen_id.box_act_screen.act_screen_screen_name.padding=(
      self.width*.01,self.act_screen_height*.01,0,0)
    self.act_screen_id.box_act_screen.act_screen_screen_name.add_act_name_label.font_size= self.width*.05
    self.act_screen_id.box_act_screen.act_screen_screen_name.email_label.font_size= self.width*.03
    self.act_screen_id.box_act_screen.act_screen_screen_name.email_label.text="  "+self.email

    #act screen add act name label
    self.act_screen_id.box_act_screen.act_name_box.padding=(
      self.width*.01,self.act_screen_height*.5,0,0)

    #date and time
    print('box_date_andtime::',self.act_screen_id.box_act_screen.box_date_and_time)
    self.act_screen_id.date_time_now=current_time_util(self.user_timezone)
    # self.act_screen_id.box_layout_date.date_input.text=self.act_screen_id.date_time_now[0]
    self.act_screen_id.box_act_screen.box_date_and_time.box_layout_date.date_input.text = self.act_screen_id.date_time_now[0]


class TableScreen(Screen):
  def __init__(self,**kwargs):
    super(TableScreen, self).__init__(**kwargs)
