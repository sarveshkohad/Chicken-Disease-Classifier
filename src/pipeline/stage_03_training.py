from src.config.configuration import ConfigurationManager
from src.components.prepare_callbacks import PrepareCallback
from src.components.training import Training
from src.logger import logging
from src.exception import MyException
import sys

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


if __name__ == "__main__":
    try:
        logging.info(f"********************")
        logging.info(f">>>>>>>{STAGE_NAME} started<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>{STAGE_NAME} completed<<<<<<<<<<<<<<<<")
    except Exception as e:
        raise MyException(e, sys)
    