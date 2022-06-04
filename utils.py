from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.button import Button
import datetime
from pytz import timezone



class CanvasWidget(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(127/255,160/255,189/255,1)
            self.rect=Rectangle(pos=self.pos,size=self.size)
            self.bind(pos=self.update_rect,
                          size=self.update_rect)
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# class invalidLogin(BoxLayout):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#
#     def ok_button(self):
#         self.parent.title.text=''
#         self.parent.note.text=''
#         self.parent.remove_widget(self)
def current_time_util(user_timezone):
    date_time_obj=datetime.datetime.now()
    date_time_obj_tz_aware=timezone(user_timezone).localize(date_time_obj)
    hour_temp=date_time_obj_tz_aware.strftime("%H")
    hour=hour_temp if hour_temp[0]!='0' else hour_temp[1]

    am_pm='AM' if int(hour)<12 else 'PM'

    hour=hour if int(hour)<13 else str(int(hour)-12)
    minute=date_time_obj_tz_aware.strftime("%M")
    # time_thing=date_time_obj_tz_aware.strftime("%H:%M%p")
    time_thing=f'{hour}:{minute} {am_pm}'
    date_thing=date_time_obj_tz_aware.strftime("%m/%d/%Y")

    date_time_now=(date_thing,time_thing)

    return(date_time_now)
