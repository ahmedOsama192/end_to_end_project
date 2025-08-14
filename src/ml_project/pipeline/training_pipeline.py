

from ml_project.components import model_trainer
from ml_project.config.configuration import ConfigurationManager
from ml_project import logger

class ModelTrainingPipeline:

    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.model_trainer_config = self.config_manager.get_model_trainer_config()
        self.model_trainer = model_trainer.ModelTrainer(config=self.model_trainer_config)
    
    def main(self):

        try:
            logger.info("Starting model training pipeline")
            self.model_trainer.train_model()
            logger.info("Model training pipeline completed successfully")
        
        except Exception as e:
            logger.exception(f"Model training pipeline failed with error: {e}")
            raise e

STAGE_NAME = "Model Training"
if __name__ == "__main__":
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()