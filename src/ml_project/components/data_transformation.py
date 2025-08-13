

import os 
from ml_project import logger   
from sklearn.model_selection import train_test_split
import pandas as pd

class DataTransformation:

    def __init__(self, config):
        self.config = config

    def scaling(self):
        try:
            # Load the data
            data_path = self.config.data_path
            data = pd.read_csv(data_path)
            logger.info("Data loaded successfully for transformation")

            # Perform scaling (example: Min-Max scaling)
            scaled_data = (data - data.min()) / (data.max() - data.min())
            logger.info("Data scaling completed")

            # Save the transformed data
            file_name = "scaled_data.csv"
            scaled_data_path = os.path.join(self.config.root_dir, file_name)
            scaled_data.to_csv(scaled_data_path, index=False)
        
            logger.info(f"Transformed data saved to {scaled_data_path}")

        except Exception as e:  
            logger.exception(f"Data transformation failed with error: {e}")
            raise e
        
        return file_name
        

    def train_test_splitting(self , file_name):
        try:
            # Load the data
            data_path = self.config.root_dir + "/" + file_name
            if not os.path.exists(data_path):
                raise FileNotFoundError(f"File not found: {data_path}")
            
            logger.info(f"Loading data from {data_path}")

            if not os.path.isfile(data_path):
                raise ValueError(f"Expected a file but found a directory: {data_path}")
            
            # Read the data
            data = pd.read_csv(data_path)
            logger.info("Data loaded successfully for transformation")

            # Perform train-test split
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logger.info("Train-test split completed")

            # Save the transformed data
            train_data_path = os.path.join(self.config.root_dir, "train_data.csv")
            test_data_path = os.path.join(self.config.root_dir, "test_data.csv")
            train_data.to_csv(train_data_path, index=False)
            test_data.to_csv(test_data_path, index=False)
            logger.info(f"Transformed data saved to {train_data_path} and {test_data_path}")

        except Exception as e:
            logger.exception(f"Data transformation failed with error: {e}")
            raise 
        
stage_name = "Data Transformation Stage"
if __name__ == "__main__":

    try: 
        logger.info(f">>>>>>>>>>>>> {stage_name} started <<<<<<<<<<<<<<<")
        data_transformation_pipeline = DataTransformation()
        data_transformation_pipeline.main()
        logger.info(f">>>>>>>>>>>>> {stage_name} completed successfully")
    except Exception as e:
        logger.exception(f">>>>>>>>>>>>> {stage_name} failed with error: {e}")
        raise e