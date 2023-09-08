import argparse
# from GUI.splash_screen import splash_screen
from Fitur.pose_estimation import pose_estimation
def main():
    parser = argparse.ArgumentParser(description='anda akan menggunakan aplikasi ini untuk machine learning atau implementasi?')
    
    # Tambahkan argumen yang diharapkan
    parser.add_argument('-klasifikasi', action='store_true', help='Jalankan mode klasifikasi')
    
    args = parser.parse_args()
    
    if args.klasifikasi:
        fitur = pose_estimation()
    # else:
        # splash = splash_screen()
        # splash.run()
if __name__ == '__main__':
    main()
