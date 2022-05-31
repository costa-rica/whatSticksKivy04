#kivy
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
from utils import CanvasWidget
#python
import json
import requests

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
    print('ParentScreen2 on_enter')
    print('size of toolbar')
    print(self.toolbar.size)


class TextInputTextSize(BoxLayout):
  textInput = ObjectProperty()
  textInputMultiline = ObjectProperty()

  def submitRequest(self):
    # Get the request from the TextInput
    # textInputTxt = self.textInputSingleLine.text
    self.textInputMultiline.text += '\n' + textInputTxt

class TextInputSpecial(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    act_screen =instance.parent.parent.parent.parent.parent.parent
    if value:
      act_screen.add_act_note_label.color=(.7,.7,.7,1)
    else:
      act_screen.add_act_note_label.color=(.3,.3,.3,1)

class TextInputAddName(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice

    act_screen =instance.parent.parent.parent.parent.parent
    print('act_screen:::', act_screen)
    if value:
      act_screen.add_act_name_label.color=(.7,.7,.7,1)
    else:
      act_screen.add_act_name_label.color=(.3,.3,.3,1)


class SuperBox(BoxLayout):...

class ActivityScreen(Screen):
  email=StringProperty('')
  username=StringProperty('')
  user_timezone=StringProperty('')
  add_act_note=ObjectProperty(None)
  add_act_note_label=ObjectProperty(None)
  email_label=ObjectProperty(None)
  def __init__(self,**kwargs):
    super(ActivityScreen,self).__init__(**kwargs)


  def change_label_color(self):
    self.ids.add_act_note_label.color=(0,1,0,1)


  def on_enter(self):
    print('ActivityScreen on_enter&&&&')
    # print('email_Label size -on_enter:::', self.email_label.texture_size)

  def get_label_size(self):
    print('email_Label_text size:::', self.email_label.texture_size)
    print('email_Label size:::', self.email_label.size)
  def resize_label_size(self):
    # self.email_label.texture_size=[150,29]
    self.email_label.size_hint=[None,None]
    self.email_label.size[0]=250
  # def text_input_state(self, widget):
  #   print('widget.focus')
  #   print(dir(widget.focus))
  #   print(widget.focus)

# class LabelEmail(Label):
#   def __init__(self,**kwargs):
#     super(LabelEmail,self).__init__(**kwargs)
#     print('**LabelEmail __init__')
#     self.text="email@.com"
#     self.font_size="24dp"
#     print('size::', self.texture_size)
#     self.size_hint=[None,None]
#     self.size[0]=self.texture_size[0]
# #
#   def on_enter(self, self2):
#     print('***LabelEmail on_enter************************')
#     print('parent:::', self.parent.parent.parent)

class TableScreen(Screen):
  def __init__(self,**kwargs):
    super(TableScreen, self).__init__(**kwargs)
