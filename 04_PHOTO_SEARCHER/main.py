'''
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
'''

import wikipedia
import requests



'''
Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        self.manager.current_screen.ids.img.source = 'files/luffy.jpg'

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

'''
print("Ok")

page = wikipedia.page("Onepiece")

link = page.images[0]
print(link)

req = requests.get(link)

with open("one_piece.jpg", 'wb') as file:
    file.write(req._content)
