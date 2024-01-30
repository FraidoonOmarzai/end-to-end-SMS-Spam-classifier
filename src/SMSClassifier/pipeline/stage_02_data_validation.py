from src.SMSClassifier.config.configuration import ConfigurationManager
from src.SMSClassifier.components.data_validation import DataValidation
from src.SMSClassifier.logging import logger


STAGE_NAME = 'Data Validation'


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exist()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
