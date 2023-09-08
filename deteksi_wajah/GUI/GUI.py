import cv2
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

class GUI(MDApp):
    def build(self):
        self.title = "Aplikasi OpenCV di Kivy"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('tampilan.kv')

    def on_start(self):
        Clock.schedule_once(self.change_to_main, 3)

    def change_to_main(self, dt):
        self.root.current = 'main'

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.image_widget = Image()
        self.add_widget(self.image_widget)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update_frame, 1.0 / 30.0)

    def update_frame(self, dt):
        ret, frame = self.capture.read()
        frame = cv2.flip(frame, -1)
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(frame_rgb.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
            self.image_widget.texture = texture

    def on_stop(self):
        self.capture.release()

if __name__ == '__main__':
    GUI().run()
