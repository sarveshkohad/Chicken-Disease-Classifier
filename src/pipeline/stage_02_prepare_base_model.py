from src.config.configuration import ConfigurationManager
from src.exception import MyException
from src.components.prepare_base_model import PrepareBaseModel
import sys
from src.logger import logging

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
    

if __name__ == "__main__":
    try:
        logging.info(f"********************")
        logging.info(f">>>>>>>{STAGE_NAME} started<<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<<<<<<")
    except Exception as e:
        raise MyException(e, sys)
    