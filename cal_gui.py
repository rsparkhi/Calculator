import re
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class CalGridLayout(GridLayout):
    pass

class CalculatorApp(App):
    def build(self):
        return CalGridLayout()

CalculatorApp().run()
