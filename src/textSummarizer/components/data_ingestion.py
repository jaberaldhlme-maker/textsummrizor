import os
import urllib.request as request
from zipfile 
from textSummarizer import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info(f"downloading file from :[{self.config.source_URL}] into :[{self.config.local_data_file}]")
        filename, headers = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
        logger.info(f"file :[{filename}] downloaded with following info: \n{headers}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)