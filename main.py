from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.logger import logging
from src.exception import MyException
import sys



STAGE_NAME= "Data Ingestion stage"

try:
        logging.info(f">>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logging.info(f">>>>>>>>>>>>>{STAGE_NAME} failed<<<<<<<<<<<<<<<<<<")
    raise MyException(e, sys)