from src.SMSClassifier.config.configuration import ConfigurationManager
from src.SMSClassifier.components.data_ingestion import DataIngestion
from src.SMSClassifier.logging import logger


STAGE_NAME = 'Data Ingestion'


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.dataIngestionConfig()
        data_ingestinion = DataIngestion(confg=data_ingestion_config)
        data_ingestinion.download_dataset()
        data_ingestinion.extract_zip()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
