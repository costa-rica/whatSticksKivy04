import os
import json

with open(os.path.join('/Users/nick/Documents/_config_files','config_wshKivy.json')) as config_file:
  config =json.load(config_file)


class Config():
  email = config.get('email')
  password = config.get('password')
