from src.SMSClassifier.config.configuration import ConfigurationManager
from src.SMSClassifier.components.model_training import ModelTraining
from src.SMSClassifier.logging import logger


STAGE_NAME = 'Model Training'


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model = ModelTraining(model_training_config)
        model.training_pipeline()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
