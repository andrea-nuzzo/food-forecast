import pandas as pd
import logging
from utils.logging import setup_logging

setup_logging()


class DataTransform:
    def __init__(self, data):
        self.data = data
        self.start_date = None
        self.end_date = None
    
    def clean_data(self):
        return self.data[self.data['vend_status'] != 'Payment Declined']
    
    def select_columns(self):
        columns_to_keep = ['timestamp', 'location__venue__name', 'product__external_id', 'name']
        return self.data[columns_to_keep]
    
    def set_date_range(self):
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'], dayfirst=True)
        date = self.data['timestamp'].dt.date
        self.start_date = date.min()
        self.end_date = date.max()

    def aggregate_products(self):
        aggregated_data = self.data.groupby(['product__external_id', 'name']).size().reset_index(name='product_quantity')
        company_name = self.data['location__venue__name'].iloc[0]
        aggregated_data['company_name'] = company_name
        return aggregated_data
    
    def transform_data(self):
        self.data = self.clean_data()
        self.data = self.select_columns()
        self.set_date_range()
        self.data = self.data.drop(columns=['timestamp'])
        self.data = self.aggregate_products()

        logging.debug(f"Completed data transformation. Data shape: {self.data.shape}")
        return self.data
    
    def get_date_range(self):
        return self.start_date.strftime('%d/%m/%Y'), self.end_date.strftime('%d/%m/%Y')