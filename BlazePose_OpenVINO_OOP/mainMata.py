import argparse
from GUI.splash_screen import splash_screen
from FItur.pengolahan_mata import pengolahan_mata
def main():
    parser = argparse.ArgumentParser(description='anda akan menggunakan aplikasi ini untuk machine learning atau implementasi?')
    
    # Tambahkan argumen yang diharapkan
    parser.add_argument('--klasifikasi', type=str, help='Argumen input')
    
    args = parser.parse_args()
    
    if args.klasifikasi:
        fitur = pengolahan_mata()
        fitur.start()
    else:
        splash = splash_screen()
        splash.run()
if __name__ == '__main__':
    main()
