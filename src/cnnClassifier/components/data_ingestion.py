import os
import shutil
import zipfile
from pathlib import Path
import kagglehub
import shutil
from cnnClassifier import logger
from cnnClassifier.utils.common import read_yaml, create_directories, get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''
        try: 
            os.environ["KAGGLEHUB_CACHE"] = self.config.root_dir
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.unzip_dir, exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # kagglehub.dataset_download(dataset_url, zip_download_dir)
            cache_path = kagglehub.dataset_download("nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone")

            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            
            for item in os.listdir(cache_path):
                s = os.path.join(cache_path, item)
                d = os.path.join("artifacts/data_ingestion", item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)

            logger.info(f"Data successfully moved to: artifacts/data_ingestion")
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
