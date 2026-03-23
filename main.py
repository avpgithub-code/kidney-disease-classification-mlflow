from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage03_model_training import ModelTrainingPipeline

if __name__ == "__main__":
    try:
        # logger.info(">>>>> Starting the pipeline <<<<<")
        # data_ingestion_pipeline = DataIngestionPipeline()
        # data_ingestion_pipeline.main()
        # logger.info(">>>>> Pipeline completed successfully <<<<<")
        
        logger.info(">>>>> Starting the Prepare Base Model Pipeline <<<<<")
        prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
        prepare_base_model_pipeline.main()
        logger.info(">>>>> Prepare Base Model Pipeline completed successfully <<<<<")
        
        logger.info(">>>>> Starting the Model Training Pipeline <<<<<")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()
        logger.info(">>>>> Model Training Pipeline completed successfully <<<<<")

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        logger.info(">>>>> Pipeline terminated with errors <<<<<")