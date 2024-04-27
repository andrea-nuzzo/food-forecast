import os
from fetch.data_loader import DataLoader
from transform.data_transform import DataTransform
from ingest.data_ingest_rolling_order import DataIngestRollingOrder
import logging
from utils.logging import setup_logging

setup_logging()

if __name__ == "__main__":

    data_dir = "../data/sales_report/"
    files = os.listdir(data_dir)
    logging.debug(f"Number of files: {len(files)}")

    for file_name in os.listdir(data_dir):
        # Load data
        file_path = os.path.join(data_dir, file_name)
        data_loader = DataLoader(file_path)
        data = data_loader.load_data()
        
        # Transform data
        data_transform = DataTransform(data)
        data = data_transform.transform_data()
        start_date, end_date = data_transform.get_date_range()
        
        # Ingest data
        data_ingest = DataIngestRollingOrder(data, start_date, end_date)
        data = data_ingest.ingest_data(data)