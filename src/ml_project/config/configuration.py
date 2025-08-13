

from ml_project.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from ml_project.utils import read_yaml, create_directories
from ml_project.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig     

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, 
                 params_filepath=PARAMS_FILE_PATH ,
                 schema_FILE_PATH=SCHEMA_FILE_PATH
                 ):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_FILE_PATH)
        self.create_directories(self.config.artifacts)

    def get_data_ingestion_config(self):

        data_inges_config = DataIngestionConfig(
            root_dir=self.config.paths.root_dir,
            source_url=self.config.paths.source_url,
            local_data_file=self.config.paths.local_data_file,
            unzip_dir=self.config.paths.unzip_dir
        )

        create_directories([data_inges_config.root_dir])

        return data_inges_config


    def get_data_validation_config(self):

        data_validation_config = DataValidationConfig(
            root_dir=self.config.data_validation.root_dir,
            unzip_dir=self.config.data_ingestion.unzip_dir,
            status_file=self.config.data_validation.status_file
        )

        schema = self.schema.Columns
        create_directories([data_validation_config.root_dir])

        return data_validation_config

    def get_data_transformation_config(self):
        data_transformation_config = DataTransformationConfig(
            root_dir=self.config.data_transformation.root_dir,
            data_path=self.config.data_ingestion.unzip_dir
        )

        create_directories([data_transformation_config.root_dir])

        return data_transformation_config
    



    
