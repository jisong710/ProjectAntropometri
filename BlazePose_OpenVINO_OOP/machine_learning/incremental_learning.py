import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle


class incremental_learning:
    def __init__(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        namafile = "file.sav"
        pickle.dump(self.model, open(namafile,"wb"))

    def incremental_learning(self,new_data, new_labels):
        self.X_train = self.X_train.append(new_data, ignore_index=True)
        self.y_train = self.y_train.append(new_labels, ignore_index=True)
        model = self.model.fit(self.X_train, self.y_train)
        namafile = "file.sav"
        pickle.dump(model, open(namafile,"wb"))
        return model

    def predict_and_display(new_data,model):
        predicted_data = model.predict(new_data)
        return predicted_data

