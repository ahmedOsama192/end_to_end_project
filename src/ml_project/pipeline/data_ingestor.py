


from ml_project.components.data_ingestion import DataIngestion
from ml_project.config.configuration import ConfigurationManager
from mlproject import logger

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.data_ingestion_config = self.config_manager.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(config=self.data_ingestion_config)

    def main(self):
        logger.info("Starting data ingestion pipeline")
        self.data_ingestion.download_data()
        self.data_ingestion.unzip_data()
        logger.info("Data ingestion pipeline completed successfully")

if __name__ == "__main__":

    try: 

        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} completed successfully")
    except Exception as e:
        logger.exception(f">>>>>>>>>>>>> {STAGE_NAME} failed with error: {e}")
        raise e