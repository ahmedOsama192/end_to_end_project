

from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_validation import DataValidation
from ml_project import logger


class DataValidationPipeline:

    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.data_validation_config = self.config_manager.get_data_validation_config()
        self.data_validation = DataValidation(config=self.data_validation_config)

    def main(self):
        logger.info("Starting data validation pipeline")
        self.data_validation.validate_data()
        logger.info("Data validation pipeline completed successfully")

STAGE_NAME = "Data Validation Stage"
if __name__ == "__main__":

    try: 

        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.main()
        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} completed successfully")
    except Exception as e:
        logger.exception(f">>>>>>>>>>>>> {STAGE_NAME} failed with error: {e}")
        raise e