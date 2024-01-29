from src.SMSClassifier.config.configuration import DataIngestionConfig
import os
import urllib.request as request
from src.SMSClassifier.logging import logger
from src.SMSClassifier.utils.common import get_size
import zipfile
from pathlib import Path

class DataIngestion:
    def __init__(self, confg: DataIngestionConfig):
        self.config = confg
        
    
    def download_dataset(self):
        
        if not os.path.exists(self.config.local_data_file):
            filename, headers= request.urlretrieve(
                                    url= self.config.data_url,
                                    filename=self.config.local_data_file
                                )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"file already exist, size--> {get_size(Path(self.config.local_data_file))}")
    
    
    def extract_zip(self):
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)