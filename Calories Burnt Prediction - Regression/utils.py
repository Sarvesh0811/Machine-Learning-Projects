import pickle
import json
import config

import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


class Calories():

    def __init__(self):
        self.__load_data()

    def __load_data(self):

        with open(config.MODEL_FILE_NAME, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.COLUMN_DATA_JSON, 'r') as f:
            self.column_data = json.load(f)

        with open(config.SCALING_FILE_NAME, 'rb') as f:
            self.scaler = pickle.load(f)

        self.column_names = self.model.feature_names_in_
        self.features_count = self.model.n_features_in_

    def predicted_calories(self, Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp):
    
        self.__load_data()

        Gender = self.column_data['Gender'][Gender]

        test_array = np.zeros((1, self.features_count))
        test_array[0, 0] = Gender
        test_array[0, 1] = Age
        test_array[0, 2] = Height
        test_array[0, 3] = Weight
        test_array[0, 4] = Duration
        test_array[0, 5] = Heart_Rate
        test_array[0, 6] = Body_Temp

        test_array = self.scaler.transform(test_array)

        predicted_calories = self.model.predict(test_array)

        return predicted_calories.tolist() 

def load_dataset():
    df = pd.read_csv(config.CSV_FILE_NAME)
    # print(df)
    return df
