from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.app import App
from kivy.clock import Clock
from kivymd.app import MDApp
import GUI

# Definisikan tampilan splash screen
splash_screens = Builder.load_string("""
BoxLayout:
    orientation: 'vertical'
    Image:
        source: 'your_splash_image.png'
""")

# Definisikan tampilan utama
main_screen = Builder.load_string("""
BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'Welcome to My App'
        halign: 'center'
""")

class splash_screen(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.screen_manager = BoxLayout()
        self.screen_manager.add_widget(splash_screens)
        Clock.schedule_once(self.switch_screen, 5)  # Ganti tampilan setelah 5 detik
        return self.screen_manager

    def switch_screen(self, dt):
        self.screen_manager.clear_widgets()
        self.screen_manager.add_widget(main_screen)

