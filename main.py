from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.logger import logging
from src.exception import MyException
import sys
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME= "Data Ingestion stage"

try:
        logging.info(f">>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<<<<")
except Exception as e:
    logging.info(f">>>>>>>>>>>>>{STAGE_NAME} failed<<<<<<<<<<<<<<<<<<")
    raise MyException(e, sys)



STAGE_NAME = "Prepare Base Model"

try:
        logging.info(f"********************")
        logging.info(f">>>>>>>{STAGE_NAME} started<<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<<<<<<")
except Exception as e:
        raise MyException(e, sys)
