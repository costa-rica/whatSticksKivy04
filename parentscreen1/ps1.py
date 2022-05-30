from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
import requests
import utils
import json
import os
# from kivymd.app import MDApp


Builder.load_file(os.path.join(os.getcwd(),'ps1.kv'))
class ParentScreen1(Screen):
  email = ObjectProperty(None)
  password = ObjectProperty(None)
  password_text = ObjectProperty(None)
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen1 initialized')
    # app = App.get_running_app()



  def on_enter(self):
    print('ParentScreen1 on_enter')


  def show_password(self, checkbox, value):
    # print('self:::', self)
    if value:
      self.password.password = False
      self.password_text.text = "Hide password"
    else:
      self.password.password = True
      self.password_text.text = "Show password"

  def login_button(self):
    # base_url= 'http://localhost:8000'

    base_url = 'https://api.what-sticks-health.com'
    response_login = requests.request('GET',base_url + '/login',
        auth=(self.email.text,self.password.text))

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
      if user_data_dict['email']==self.email.text:
      # if user_data_dict['email']==1:
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
        self.screens_dict['parent_screen_2'].email=self.email.text
        self.screens_dict['parent_screen_2'].username=self.username
        self.screens_dict['parent_screen_2'].user_timezone=self.user_timezone

      else:
        print('failbox')
        self.add_widget(FailBox())

class FailBox(BoxLayout):...
