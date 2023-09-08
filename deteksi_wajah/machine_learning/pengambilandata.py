from tensorflow.keras.utils import Sequence
import numpy as np
import random

class CustomDataGenerator(Sequence):
    def __init__(self, image_paths, labels, preprocess_function, batch_size=32, shuffle=True):
        self.image_paths = image_paths
        self.labels = labels
        self.preprocess_function = preprocess_function
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.on_epoch_end()

    def __len__(self):
        return int(np.ceil(len(self.image_paths) / self.batch_size))

    def __getitem__(self, index):
        batch_image_paths = self.image_paths[index * self.batch_size : (index + 1) * self.batch_size]
        batch_labels = self.labels[index * self.batch_size : (index + 1) * self.batch_size]
        
        batch_images = [self.preprocess_function(image_path) for image_path in batch_image_paths]
        batch_labels = np.array(batch_labels)
        
        return np.array(batch_images), batch_labels

    def on_epoch_end(self):
        if self.shuffle:
            c = list(zip(self.image_paths, self.labels))
            random.shuffle(c)
            self.image_paths, self.labels = zip(*c)
