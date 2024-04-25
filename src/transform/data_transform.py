import pandas as pd
import logging
from utils.logging import setup_logging

setup_logging()


class DataTransform:
    def __init__(self, data):
        self.data = data
    
    def clean_data(self, data):
        # Delete rows where payment has been refused
        return data[data['vend_status'] != 'Payment Declined']
    
    def select_columns(self, data):
        columns_to_keep = ['timestamp', 'location__venue__name', 'product__external_id', 'name']
        return data[columns_to_keep]
    
    def aggregate_products(self, data):
        aggregated_data = data.groupby(['product__external_id', 'name']).size().reset_index(name='product_quantity')
        return aggregated_data
    
    def transform_data(self, data):
        data = self.clean_data(self.data)
        data = self.select_columns(data)
        
        data['timestamp'] = pd.to_datetime(data['timestamp'], dayfirst=True)
        date = data['timestamp'].dt.date
        
        start_date = date.min().strftime('%d/%m/%Y')
        end_date = date.max().strftime('%d/%m/%Y')
        transaction_range = f"{start_date} - {end_date}"
        data = data.drop(columns=['timestamp'])
        
        data = self.aggregate_products(data)
        
        data['transaction_range'] = transaction_range
        
        logging.debug(f"Completed data transformation. Data shape: {data.shape}")
        
        return data