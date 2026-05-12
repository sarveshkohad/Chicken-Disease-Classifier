import urllib.request as request
import zipfile
from src.logger import logging
import py7zr
import os

class DataIngestion:
    def __init__(self, DataIngestionConfig):
        self.config = DataIngestionConfig

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers= request.urlretrieve(
                url = self.config.source_URL,
                filename=self.config.local_data_file
            )
            logging.info(f"{filename} download with following info: \n:{headers}")

        else:
            logging.info(f"File already exists!:{self.config.local_data_file}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts zip file into data directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with py7zr.SevenZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)