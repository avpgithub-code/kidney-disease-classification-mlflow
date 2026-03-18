from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepaara_base_model import PrepareBaseModel

STAGE_NAME = "STAGE02_PREPARE_BASE_MODEL"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        logger.info(f"Started {STAGE_NAME}")
        prepare_base_model_config = self.config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)

        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

        logger.info(f"Completed {STAGE_NAME}")

if __name__ == "__main__":
    try:
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e