from src.SMSClassifier.constants import CONFIG_PATH
from src.SMSClassifier.utils.common import read_yaml, create_directories
from src.SMSClassifier.entity.config_entity import (DataIngestionConfig,
                                                    DataValidationConfig)


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
