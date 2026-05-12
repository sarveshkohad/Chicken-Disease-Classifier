from src.config.configuration import ConfigurtionManager
from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import MyException
import sys


STAGE_NAME= "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurtionManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise MyException(e, sys)
        

if __name__ == '__main__':
    try:
        logging.info(f">>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logging.info(f">>>>>>>>>>>>>{STAGE_NAME} failed<<<<<<<<<<<<<<<<<<")
        raise MyException(e, sys)