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
    df: Path
