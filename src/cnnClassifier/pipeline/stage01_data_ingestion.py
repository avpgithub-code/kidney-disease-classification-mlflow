from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        
    def main(self):
        try:
            logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            # data_ingestion.extract_zip_file()
            logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")
        except Exception as e:
            logger.error(f"Error in stage {STAGE_NAME}: {e}")
            raise e

if __name__ == "__main__":
    obj = DataIngestionPipeline()
    obj.main()