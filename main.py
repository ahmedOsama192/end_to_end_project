

from src import logger
from src.ml_project.pipeline.data_ingestor import DataIngestionPipeline
from src.ml_project.pipeline.data_validation import DataValidationPipeline



STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":

    try: 

        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} completed successfully")
    except Exception as e:
        logger.exception(f">>>>>>>>>>>>> {STAGE_NAME} failed with error: {e}")
        raise e
    
    
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