import os 
from ml_project import logger
import pandas as pd
from ml_project.entity.config_entity import DataValidationConfig



class DataValidation :
    
    def __init__(self , config: DataValidationConfig):
        self.config = config

    def validate_data(self):

        try :

            validate_status = None

            data = pd.read_csv(self.config.unzip_dir)
            all_cols = list(data.columns)
            schema_cols = self.config.schema.columns
            logger.info("Data loaded successfully for validation")

            if len(all_cols) == len(schema_cols):
                if set(all_cols) == set(schema_cols):
                    validate_status = True
                    logger.info("Data validation successful: All columns match the schema")
                else:
                    validate_status = False
                    logger.warning("Data validation failed: Columns do not match the schema")
            else:
                validate_status = False
                logger.warning("Data validation failed: Number of columns do not match the schema")

            with open(self.config.status_file, 'w') as f:
                f.write("Validation Status: " + str(validate_status) + "\n")
                f.write("Columns in Data: " + str(all_cols) + "\n")
                f.write("Schema Columns: " + str(schema_cols) + "\n")

        except Exception as e:
            logger.exception(f"Data validation failed with error: {e}")
            raise e
