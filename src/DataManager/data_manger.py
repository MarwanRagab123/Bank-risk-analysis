import pandas as pd
import os

class DataManagerc:
    def __init__(self):
        pass


    def load_data(self,path_file):
        if not os.path.exists(path_file):
            raise FileNotFoundError(f"The file {path_file} does not exist.")

        try:
            data=pd.read_csv(path_file)
            return data
        except pd.errors.EmptyDataError:
            raise f"the file {path_file} is Empty!"

    def clean_data(self,data):

            if data is not None:
                data.dropna(inplace=True)
                data.drop_duplicates(inplace=True)
                return data
            else:
                print("Data not loaded. Please load data before cleaning!!\n")








