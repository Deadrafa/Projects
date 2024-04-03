from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


from kivy.core.window import Window
Window.size = (512, 512)
Window.clearcolor = (255/255, 145/255, 1/255, 2)
Window.title = 'Чмо ебанное'

class MyApp(App):

    '''def __init__(self, **kwargs):
        super().__init__()
        self.label = Label(text='Привет\nПошёл на хуй')'''

    def build(self):
        self.number = 0
        self.box = BoxLayout(orientation='vertical')
        
        self.button = Button(text='Нажми меня', background_down = '')
        self.button.bind(on_press=self.klik)
        self.box.add_widget(self.button)

        return self.box

    def klik(self, *instance):
        self.number += 1
        if self.number == 5:
            self.new_button1 = Button(background_normal = 'etap1.png',background_down = '', on_press=self.klik)
            self.box.remove_widget(self.button)
            self.box.add_widget(self.new_button1)


        elif self.number == 10:
            self.new_button2 = Button(background_normal = 'etap2.png',background_down = '', on_press=self.klik)
            self.box.remove_widget(self.new_button1)
            self.box.add_widget(self.new_button2)

        elif self.number == 15:
            self.new_button3 = Button(background_normal = 'etap3.png',background_down = '', on_press=self.klik)
            self.box.remove_widget(self.new_button2)
            self.box.add_widget(self.new_button3)

        elif self.number == 20:
            self.new_button4 = Button(background_normal = 'etap4.png',background_down = '', on_press=self.klik)
            self.box.remove_widget(self.new_button3)
            self.box.add_widget(self.new_button4)

        elif self.number == 25:
            self.new_button5 = Button(background_normal = 'etap5.png',background_down = '', on_press=self.klik)
            self.box.remove_widget(self.new_button4)
            self.box.add_widget(self.new_button5)
        
        elif self.number == 30:
            self.new_button6 = Button(background_normal = 'etap6.png',background_down = '', on_press=self.klik)
            self.box.remove_widget(self.new_button5)
            self.box.add_widget(self.new_button6)

        elif self.number == 33:
            self.finish = Button(text = "На этом всё", on_press=self.klik)
            self.box.remove_widget(self.new_button6)
            self.box.add_widget(self.finish)

if __name__ == '__main__':
    MyApp().run()