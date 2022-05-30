from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.button import Button

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
