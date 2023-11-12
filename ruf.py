from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from instructions import *

name = 0
age = 0
p1,p2,p3 = 0,0,0

class InstrScreen(Screen):
    def __init__(self, **kwargs):
        instrution = Label(text = txt_instruction)
        nametxt = Label(text = 'Введите Имя:')
        self.in_name = TextInput(multiline=False)
        name = self.in_name.text
        agetxt = Label(text = 'Введите возраст:')
        self.in_age = TextInput(multiline=False)
        age = self.in_age.text
        self.btn = Button(text = 'Начать', size_hint = (0.3, 0.2), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
        v1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        h1 = BoxLayout(padding = 8, spacing = 8)
        h2 = BoxLayout(padding = 8, spacing = 8)
        v1.add_widget(instrution)
        h1.add_widget(nametxt)
        h1.add_widget(self.in_name)
        h2.add_widget(agetxt)
        h2.add_widget(self.in_age)
        v1.add_widget(h1)
        v1.add_widget(h2)
        v1.add_widget(self.btn)
    def next(self):
        global name
        global age
        self.manager.current = ResultScr

class ResultScr(Screen):
    def __init__(self, **kwargs):
        instruction = Label(text = txt_test1)
        resulttxt = Label(text = 'Введите результат:')
        self.in_result = TextInput(multiline=False)
        self.in_result = p1
        self.btn = Button(text = 'Продолжить', size_hint = (0.3, 0.2), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
        v1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        h1 = BoxLayout(padding = 8, spacing = 8)
        v1.add_widget(instruction)
        h1.add_widget(resulttxt)
        h1.add_widget(self.in_result)
        v1.add_widget(h1)
        v1.add_widget(self.btn)
    def next(self):
        global p1
        self.manager.current = PrisedScr

class PrisedScr(Screen):
    def __init__(self, **kwargs):
        instruction = Label(text = txt_sits)
        self.btn = Button(text = 'Продолжить', size_hint = (0.3, 0.2), pos_hint = {'center_x' : 0.5})
        self.btn.on_press = self.next
        v1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        v1.add_widget(instruction)
        v1.add_widget(self.btn)
    def next(self):
        self.manager.current = AfterResultScr

class AfterResultScr(Screen):
    def __init__(self, **kwargs):
        instruction = Label(text = txt_test3)
        resbef = Label(text = '')


class HeartCheck(App):
    def build(self):  
        sm = ScreenManager()
        sm.add_widget(InstrScreen(name = 'inst'))
        sm.add_widget(ResultScr(name = 'res'))
        sm.add_widget(PrisedScr(name = 'pris'))
        sm.add_widget(AfterResultScr(name = 'afterres'))
        return sm

app = HeartCheck()
app.run()