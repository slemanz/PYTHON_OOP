from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests



# Use the obtained User-Agent string
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}



Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        # get user query from textinput
        query = self.manager.current_screen.ids.user_query.text

        # get wikipedia page and the first image link
        page = wikipedia.page(query)

        image_link = page.images[0]
        for x in range(0, len(page.images)):
            if ('png' in image_link[x]) or ('jpg' in image_link[x]):
                image_link = page.images[x]
                break

        # Download the image
        req = requests.get(image_link, headers=headers)
        imagepath = 'files/image.jpg'

        print(req.status_code)

        with open(imagepath, 'wb') as file:
            file.write(req.content)


        # set the image in the image widget
        self.manager.current_screen.ids.img.source = imagepath


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

