from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from translate import Translator

class TranslatorScreen(Screen):
    def __init__(self, **kwargs):
        super (TranslatorScreen, self).__init__(**kwargs)
        self.translator = Translator(from_lang="fr", to_lang="en")
        
        layout = BoxLayout(orientation='vertical',padding=10,spacing=10)
        self.add_widget(layout)

        # Input Field for french text
        self.input_text = TextInput(hint_text="Enter text in French",size_hint= (1,0.2),multiline=True)
        layout.add_widget(self.input_text)

        # Button to translate
        translate_button = Button(text="Translate to English", size_hint=(1,0.2))
        translate_button.bind(on_press=self.translate_text)
        layout.add_widget(translate_button)

        # Output Label
        self.output_label = Label(text="Translation will appear here",size_hint= (1,0.6))
        layout.add_widget(self.output_label)


    def translate_text(self,instance):
        french_text = self.input_text.text #Get Input Text
        if french_text.strip():
            try:
                # Perform translation
                translation = self.translator.translate(french_text)
                self.output_label.text = translation
            except Exception as e:
                self.output_label.text = f"Error: {str(e)}"
            
        else:
            self.output_label.text = "Please enter text to translate."

class MainApp(App):
    def build(self):
        return TranslatorScreen()

MainApp().run()
