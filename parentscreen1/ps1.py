from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
import requests
import utils
import json
import os
from kivy.core.window import Window

Builder.load_file(os.path.join(os.getcwd(),'parentscreen1','ps1_new.kv'))


class ParentScreen1(Screen):
  email_text = StringProperty(None)
  password_text = StringProperty(None)
  email_field = ObjectProperty(None)
  password_field = ObjectProperty(None)
  password_flag_text =ObjectProperty(None)
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen1 initialized')
    self.window_width=int(Window.size[0])
    self.window_height=int(Window.size[1])
    print('self.window_width::',type(self.window_width),self.window_width)
    print('self.window_height::',type(self.window_height),self.window_height)

    #Load email and password
    # from config import Config
    # config_stuff = Config()
    # self.email_text = Config().email
    # self.password_text = Config().password

  def on_enter(self):
    print('ParentScreen1 on_enter')

  def show_password(self, checkbox, value):
    # print('self:::', self)
    if value:
      self.password_field.password = False
      self.password_flag_text.text = "Hide password"
      # print('checkbox -dir')
      # print(dir(checkbox))
    else:
      self.password_field.password = True
      self.password_flag_text.text = "Show password"

  def login_button(self):
    # base_url= 'http://localhost:8000'

    base_url = 'https://api.what-sticks-health.com'
    response_login = requests.request('GET',base_url + '/login',
        auth=(self.email_field.text,self.password_field.text))
    print('response_login.status_code:::', response_login.status_code)
    if response_login.status_code ==200:
      login_token = json.loads(response_login.content.decode('utf-8'))['token']
      print('login_token accepted!')

      url_user_data = base_url + "/user_account_data"
      headers = {'x-access-token': login_token,'Content-Type': 'application/json'}
      response_user_data = requests.request("GET", url_user_data, headers=headers)
      user_data_dict = json.loads(response_user_data.text)
      print(json.loads(response_user_data.text))
      # print(type(json.loads(response_user_data.text)))

      # for i in user_data_dict:
      if user_data_dict['email']==self.email_field.text:

        print('self.parent.screens:::', self.parent.screens)
        self.parent.current="parent_screen_2"
        self.screens_dict={i.name: i for i in self.parent.screens}
        print('self.screens_dict.keys::')
        print(self.screens_dict.keys())
        self.id=user_data_dict['id']
        self.username=user_data_dict['username']
        self.user_timezone=user_data_dict['user_timezone']

        self.screens_dict['parent_screen_2'].login_token=login_token
        self.screens_dict['parent_screen_2'].id=self.id
        self.screens_dict['parent_screen_2'].email=self.email_field.text
        self.screens_dict['parent_screen_2'].username=self.username
        self.screens_dict['parent_screen_2'].user_timezone=self.user_timezone

    else:
      print('failbox')
      self.add_widget(FailBox())

class FailBox(BoxLayout):...
