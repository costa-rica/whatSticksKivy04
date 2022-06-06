from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from utils import current_time_util
import datetime
import activityscreen.date_and_time
from kivymd.app import MDApp
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
    # self.ps2_height=''
    # self.user_timezone=MDApp.get_running_app.myscreen.user_timezone


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


class TextInputAddName(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    print('***TextInputAddName***')
    boxlayout_act_screen =instance.parent.parent.parent.parent#different hiearchey than TextInputDynamicActNote
    if value:
      boxlayout_act_screen.act_name_box.add_act_name_label.color=(0,0,0,1)
    else:
      boxlayout_act_screen.act_name_box.add_act_name_label.color=(.3,.3,.3,1)


class TextInputDynamicActNote(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    boxlayout_act_screen =instance.parent.parent.parent.parent#different hiearchey than TextInputAddName
    print('boxlayout_act_screen:::', boxlayout_act_screen)
    #get boxlayout_act_screen.act_note_box height
    # boxlayout_act_screen.act_note_box
    print('add_act_note.height:::',boxlayout_act_screen.act_note_box.add_act_note.height)
    # above_height = boxlayout_act_screen.act_note_box.add_act_note.height
    # my_height=boxlayout_act_screen.box_date_and_time.anchor_date_time.height

    # boxlayout_act_screen.box_date_and_time.anchor_date_time.height =

    #get height of act_screen screen name boxlayout

    #get height of act_screen add act boxlayout

    #get hiehgt of act_screen add not boxlayout

    #set height of act_screen box_date_and_time remainder of act_screen boxlayout - above 3 heights

    if value:
      boxlayout_act_screen.act_note_box.add_act_note_label.color=(0,0,0,1)
    else:
      boxlayout_act_screen.act_note_box.add_act_note_label.color=(.3,.3,.3,1)
