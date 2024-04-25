import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        if self.file_path.endswith('.xlsx'): 
            data = pd.read_excel(self.file_path)
            print(data)
            return data
        raise ValueError("The file format must be Excel with the extension '.xlsx'")
            
