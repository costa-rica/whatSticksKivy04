from utils import CanvasWidget, current_time_util

class MyScreen():
  def __init__(self,**kwargs):
    super(MyScreen,self).__init__(**kwargs)
    print('MyScreen __init__')
    self.toolbar_height=1
    self.act_screen_height=1

  def send_to_act_screen(self,act_screen):
    print('MyScreen:send_to_act_screen')
    #Get Variables
    act_screen.username=self.username
    act_screen.username=self.username
    act_screen.email=self.email

    #set height of act_screen by setting the two boxlayouts that fill the screen
    act_screen.box_act_screen.height = self.act_screen_height#The screen w/ all important stuff
    act_screen.box_act_extra.height = self.act_screen_height *.25#extra filler for scroll

    #set Activity Screen screen name
    act_screen.box_act_screen.act_screen_screen_name.padding=(
      act_screen.width*.01,self.act_screen_height*.01,0,0)#left,top,right,bottom
    act_screen.box_act_screen.act_screen_screen_name.add_act_name_label.font_size= act_screen.width*.05
    #set email at top of ActivityScreen
    act_screen.box_act_screen.act_screen_screen_name.email_label.text="  "+self.email
    act_screen.box_act_screen.act_screen_screen_name.email_label.font_size=act_screen.width*.03

    #set Activity Screen act name label and input
    act_screen.box_act_screen.act_name_box.padding=(
      act_screen.width*.05,self.act_screen_height*.5,act_screen.width*.05,0)
    act_screen.box_act_screen.act_name_box.add_act_name_label.font_size=act_screen.width*.05
    act_screen.box_act_screen.act_name_box.add_act_name.font_size=act_screen.width*.03


    #act screen add act note label and input
    act_screen.box_act_screen.act_note_box.padding=(
      act_screen.width*.05,self.act_screen_height*.05,act_screen.width*.05,0)
    act_screen.box_act_screen.act_note_box.add_act_note_label.font_size=act_screen.width*.05

    act_screen.box_act_screen.act_note_box.add_act_note.textInputMultiline.font_size=act_screen.width*.03
    print('act_screen.box_act_screen.act_note_box.add_act_note.height:::', act_screen.box_act_screen.act_note_box.add_act_note.height)

    #date and time

    date_time_now=current_time_util()

    act_screen.box_act_screen.box_date_and_time.box_layout_date.date_input.text = date_time_now[0]
