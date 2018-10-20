import TextToSpeech
import TextPredictor

from kivy.app import App

from kivy.core.window import Window

from kivy.config import Config

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

from kivy.properties import NumericProperty

class KeyboardWidget(GridLayout):
    int_button_width = 250
    int_button_height = 100
    int_button_font_size = 40

    button_width = NumericProperty(int_button_width)
    button_height = NumericProperty(int_button_height)
    button_font_size = NumericProperty(int_button_font_size)

    Window.size = (int_button_width * 5,
        int_button_height * 4.0)

    def calc_error(self, error, calc_entry):
        content = BoxLayout(orientation='vertical')
        scrollview = ScrollView()

        close_popup = Button(text='Close this popup')
        error_message = Label(text=str(error))

        scrollview.add_widget(error_message)
        content.add_widget(scrollview)
        content.add_widget(close_popup)

        popup = Popup(title='An error occured',
            content=content, size_hint=(.8, .8))

        close_popup.bind(on_release=popup.dismiss)
        popup.open()

    def calculate(self, *args):
        calc_entry = self.ids.calc_input.text
        if calc_entry != '':
            if calc_entry[0] in '1234567890-+':
                try:
                    ans = str(eval(calc_entry))
                    self.ids.calc_input.text = ans
                except Exception as error:
                    self.calc_error(error, calc_entry)
                    pass

    def delete(self, *args):
        self.ids.calc_input.text = self.ids.calc_input.text[:-1]

    def clear(self, *args):
        self.ids.calc_input.text = ''
		
	#used to update the text from the quickselect menu
    def updateT(self,text):
	    self.ids.calc_input.text += text	#appends the text to the inputbar

    def speak(self, *args):
        sentence = self.ids.calc_input.text
        TextToSpeech.Speak(sentence)
        
    def predict(self, *args):
        word = self.ids.calc_input.text.split()[-1]
        NextWordArr = TextPredictor.PredictNext(word)
        self.ids.pred_1.text = NextWordArr[0][0]
        self.ids.pred_2.text = NextWordArr[1][0]
        self.ids.pred_3.text = NextWordArr[2][0]

    #def enter(self, *args):


class KeyboardApp(App):
    def build(self):
        Config.set('graphics', 'resizable', '0')
        Config.write()
        return KeyboardWidget()

if __name__ == '__main__':
    KeyboardApp().run()
