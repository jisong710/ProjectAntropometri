# from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
class GUI(MDApp):
    def build(self):
        return Builder.load_file('tampilan.kv')
    def on_start(self):
        # Set timer untuk berpindah ke halaman utama setelah 3 detik (contohnya)
        Clock.schedule_once(self.change_to_main, 2)  # Ganti 3 dengan jumlah detik yang Anda inginkan

    def change_to_main(self, dt):
        # Kode untuk berpindah ke halaman utama
        self.root.current = 'main'
if __name__ == '__main__':
    GUI().run()