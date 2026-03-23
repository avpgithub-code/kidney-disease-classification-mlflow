from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.training_config = self.config.get_training_config()

    def main(self):
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")

if __name__ == "__main__":
    try:
        pipeline = ModelTrainingPipeline()
        pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e