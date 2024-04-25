import os
from fetch.data_loader import DataLoader

if __name__ == "__main__":

    data_dir = "../data/raw/"
    for file_name in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file_name)
        data_loader = DataLoader(file_path)
        data = data_loader.load_data()