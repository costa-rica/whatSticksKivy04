from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from utils import current_time_util
import datetime

Builder.load_file('activityscreen/date_and_time.kv')

class BoxLayoutDateAndTime(BoxLayout):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
