from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.config import Config


class Example(RecycleView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.data= [{'text':str(i)}for i in range(20)]

class ImageExample(RecycleDataViewBehavior,GridLayout):
    index =0
    text=StringProperty()
    def refresh_view_attrs(self, rv, index, data):
        self.index=index
        super(ImageExample, self).refresh_view_attrs(rv, index, data)





class WidgetsExample(GridLayout):
    count = 1
    count_enable = BooleanProperty(False)
    my_text= StringProperty("1")
    text_input_str = StringProperty("Foo")
    #slider_value_txt= StringProperty("Value")


    def on_button_click(self):
        print("Button Clicked")
        if self.count_enable:
            self.count+=1
            self.my_text = str(self.count)
         
    def on_toggle_button_press(self, widget):
        print("Toggle state: "+widget.state) 
        if widget.state == "normal":
            widget.text="OFF"
            self.count_enable=False
        else:
            widget.text="ON"
            self.count_enable=True
    
    def on_switch_active(self,widget):
        print("Switch: "+str(widget.active))

    def on_slider_value(self,widget):
        print("Slider: "+str(int(widget.value)))
      #  self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self,widget):
        self.text_input_str= widget.text



class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation="lr-bt" 
        for i in range(0,100):
            size= dp(100)
            b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
            self.add_widget(b)



class AnchorLayoutExample(AnchorLayout): 
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2= Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

#Config.set('graphics', 'width', '360')

#Config.set('graphics', 'height', '740')

TheLabApp().run()
