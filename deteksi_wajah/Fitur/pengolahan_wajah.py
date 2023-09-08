import os
import cv2
import pandas as pd
from machine_learning.pengambilandata import CustomDataGenerator
from machine_learning.classification_sepaket import classification_sepaket
class pengolahan_wajah:
    def __init__(self):
        self.data = []
        self.labels = []
        dataset_berjerawat = './dataset/wajah/muka berjerawat'
        dataset_bopeng = './dataset/wajah/muka berjerawat'
        dataset_mulus = './dataset/wajah/muka mulus'
        for filename in os.listdir(dataset_berjerawat):
            if filename.endswith('.jpg'):  # Sesuaikan dengan format gambar Anda
                image_path = os.path.join(dataset_berjerawat, filename)
                label = 'berjerawat'# Misalnya, ambil label dari nama file

                # Membaca gambar dengan OpenCV
                image = cv2.imread(image_path)
                # Anda juga bisa menambahkan pra-pemrosesan lain di sini jika diperlukan

                self.data.append(image)
                self.labels.append(label)
        for filename in os.listdir(dataset_bopeng):
            if filename.endswith('.jpg'):  # Sesuaikan dengan format gambar Anda
                image_path = os.path.join(dataset_bopeng, filename)
                label = 'tidak_rata'# Misalnya, ambil label dari nama file

                # Membaca gambar dengan OpenCV
                image = cv2.imread(image_path)
                # Anda juga bisa menambahkan pra-pemrosesan lain di sini jika diperlukan

                self.data.append(image)
                self.labels.append(label)
        for filename in os.listdir(dataset_mulus):
            if filename.endswith('.jpg'):  # Sesuaikan dengan format gambar Anda
                image_path = os.path.join(dataset_mulus, filename)
                label = 'mulus'# Misalnya, ambil label dari nama file
                # Membaca gambar dengan OpenCV
                image = cv2.imread(image_path)
                # Anda juga bisa menambahkan pra-pemrosesan lain di sini jika diperlukan
                self.data.append(image)
                self.labels.append(label)
        # Mengubah data ke dalam format pandas DataFrame
        self.data_df = pd.DataFrame({'Image': self.data, 'Label': self.labels})
    def start(self):
        print(self.dataset)