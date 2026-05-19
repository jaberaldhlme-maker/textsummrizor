from textSummarizer import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import DataIngestionConfig



class ConfiguartionManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        self.config = read_yaml(config_file_path)
        logger.info(f"Configuration file {config_file_path} loaded successfully.")
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.config.data_ingestion
            logger.info("Data Ingestion configuration retrieved successfully.")
            return DataIngestionConfig(
                root_dir=data_ingestion_config.root_dir,
                source_URL=data_ingestion_config.source_URL,
                local_data_file=data_ingestion_config.local_data_file,
                unzip_dir=data_ingestion_config.unzip_dir
            )
        except Exception as e:
            logger.error(f"Error retrieving Data Ingestion configuration: {e}")
            raise e