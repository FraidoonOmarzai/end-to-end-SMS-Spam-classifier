from src.SMSClassifier.constants import CONFIG_PATH
from src.SMSClassifier.utils.common import read_yaml, create_directories
from src.SMSClassifier.entity.config_entity import (DataIngestionConfig,
                                                    DataValidationConfig,
                                                    DataTransformationConfig,
                                                    ModelTrainingConfig,
                                                    ModelEvaluationConfig)


class ConfigurationManager:
    def __init__(self, config_file=CONFIG_PATH):
        self.config_path = read_yaml(config_file)

        create_directories([self.config_path.artifacts_root])

    def dataIngestionConfig(self) -> DataIngestionConfig:
        config = self.config_path.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            data_url=config.data_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation(self) -> DataValidationConfig:
        config = self.config_path.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_dir=config.unzip_dir,
            status=config.status
        )
        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config_path.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config_path.model_training
        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            train_path=config.train_path,
        )
        return model_training_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config_path.model_evaluation
        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_path=config.test_path,
            model_path=config.model_path,
            experiment_name=config.experiment_name,
            mlflow_uri=config.mlflow_uri,
            run_name=config.run_name,
            metric_file_name = config.metric_file_name
        )
        return model_evaluation_config
