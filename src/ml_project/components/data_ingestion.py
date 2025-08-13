


import os
from urlib.requests import urlretrieve
from zipfile import ZipFile
from ml_project import logger
from ml_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        logger.info("Downloading data from source URL")
        file_name , headers = urlretrieve(url = self.config.source_url, 
                    file_name = self.config.local_data_file)
        logger.info(f"{file_name} downloaded with the following info: \n{headers}")
        logger.info(f"Data downloaded to {self.config.local_data_file}")



    def unzip_data(self):

        logger.info("Unzipping data")
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Data unzipped to {self.config.unzip_dir}")

