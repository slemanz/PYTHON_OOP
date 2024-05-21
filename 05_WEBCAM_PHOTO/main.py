from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

from filesave import FileSave


Builder.load_file('frontend.kv')






class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime("%Y%m%d-%H%M%S")
        filepath = "files/image_"+ current_time +".png"
        self.ids.camera.export_to_png(filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = filepath



class ImageScreen(Screen):
    def back(self):
        self.manager.current = 'camera_screen'



class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()



MainApp().run()