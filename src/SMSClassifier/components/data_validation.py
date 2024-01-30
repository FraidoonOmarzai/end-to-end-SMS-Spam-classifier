from src.SMSClassifier.entity.config_entity import DataValidationConfig
import os


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None

            if os.path.exists(self.config.unzip_dir):
                validation_status = True
                with open(self.config.status, 'w') as f:
                    f.write(f"Validation status (file exists): {validation_status}")
            else:
                validation_status = False
                with open(self.config.status, 'w') as f:
                    f.write(f"Validation status (file exists): {validation_status}")

            return validation_status

        except Exception as e:
            raise e
