from src.SMSClassifier.config.configuration import ConfigurationManager
from src.SMSClassifier.components.model_evaluation import ModelEvaluation
from src.SMSClassifier.logging import logger


STAGE_NAME = 'Model Evaluation'


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        evaluation = ModelEvaluation(model_evaluation_config)
        evaluation.model_evaluation()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
