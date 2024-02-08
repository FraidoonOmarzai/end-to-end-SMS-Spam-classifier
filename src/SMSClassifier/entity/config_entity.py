from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    data_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_dir: Path
    status: str


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass
class ModelTrainingConfig:
    root_dir: Path
    train_path: Path


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_path: Path
    model_path: Path
    experiment_name: str
    mlflow_uri: str
    run_name: str
    metric_file_name: str
