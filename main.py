from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline

if __name__ == "__main__":
    try:
        logger.info(">>>>> Starting the pipeline <<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info(">>>>> Pipeline completed successfully <<<<<")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        logger.info(">>>>> Pipeline terminated with errors <<<<<")