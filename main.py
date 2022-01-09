from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

class WindowOne(Screen):
    window1_label = StringProperty("Current Label")

class WindowTwo(Screen):
    def label_change(self):
        self.manager.get_screen('window1').window1_label = self.ids.txtinput.text

class MainApp(App):
    def build(self):
        return ScreenManager()

MainApp().run()
