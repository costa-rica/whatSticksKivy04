from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from utils import current_time_util
import datetime
import activityscreen.date_and_time

Builder.load_file('activityscreen/act_screen.kv')


class ActivityScreen(Screen):
  email=StringProperty('')
  username=StringProperty('')
  user_timezone=StringProperty('')
  box_act_screen=ObjectProperty()
  act_screen_screen_name=ObjectProperty()
  add_act_note=ObjectProperty(None)
  add_act_note_label=ObjectProperty(None)
  email_label=ObjectProperty(None)
  box_layout_date=ObjectProperty(None)
  box_layout_time=ObjectProperty(None)
  # user_timezone='US/Eastern'
  user_timezone=''
  def __init__(self,**kwargs):
    super(ActivityScreen,self).__init__(**kwargs)
    print('ActivityScreen __init__')
    self.ps2_height=''


  def on_enter(self):
    print("Act Screen on_enter")
    print('self.email:::', self.email)
    print('self.ps2_height:::', self.ps2_height)
    # self.date_time_obj=datetime.datetime.now()

class BoxLayoutScreenName(BoxLayout):
  def __init__(self,**kwargs):
    super(BoxLayoutScreenName, self).__init__(**kwargs)


  def on_enter(self):
    self.padding=(15,100,0,0)

class BoxLayoutActScreen(BoxLayout):
  act_name_box=ObjectProperty()
  box_layout_date=ObjectProperty()
  box_layout_time=ObjectProperty()
  act_note_box=ObjectProperty()

  def __init__(self,**kwargs):
    super().__init__(**kwargs)

class TextInputDynamicActNote(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    act_screen =instance.parent.parent.parent.parent.parent.parent
    if value:
      act_screen.act_note_box.add_act_note_label.color=(0,0,0,1)
    else:
      act_screen.act_note_box.add_act_note_label.color=(.3,.3,.3,1)


class TextInputAddName(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    act_screen =instance.parent.parent.parent.parent.parent
    print('act_screen:::', act_screen)
    if value:
      act_screen.act_name_box.add_act_name_label.color=(0,0,0,1)
    else:
      act_screen.act_name_box.add_act_name_label.color=(.3,.3,.3,1)
