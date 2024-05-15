from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests



Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        # get user query from textinput
        query = self.manager.current_screen.ids.user_query.text

        # get wikipedia page and the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]

        # Download the image
        req = requests.get(image_link)
        print(image_link)
        imagepath = 'files/image.jpg'

        print(req._content)

        """
        with open(imagepath, 'wb') as file:
            file.write(req._content)
        """


        # set the image in the image widget
        self.manager.current_screen.ids.img.source = imagepath


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

