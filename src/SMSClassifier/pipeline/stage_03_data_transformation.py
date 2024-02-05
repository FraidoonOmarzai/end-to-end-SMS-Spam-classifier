from src.SMSClassifier.config.configuration import ConfigurationManager
from src.SMSClassifier.components.data_transformation import DataTransformation1
from src.SMSClassifier.logging import logger


STAGE_NAME = 'Data Transformation'


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation1(data_transformation_config)
        df = data_transformation.clean_data()
        df = data_transformation.tfidf_vectorizer(df)
        data_transformation.train_test_splits(df)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
