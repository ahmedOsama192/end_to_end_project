

import os 
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from ml_project import logger
import joblib
from ml_project.utils.common import save_json

class ModelEvaluation:

    def __init__(self, config):
        self.config = config

    def evaluate_model(self):
        try:
            # Load the model
            model_path = self.config.model_path
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found: {model_path}")
            
            model = joblib.load(model_path)
            logger.info("Model loaded successfully")

            # Load the test data
            test_data_path = self.config.test_data_path
            if not os.path.exists(test_data_path):
                raise FileNotFoundError(f"Test data file not found: {test_data_path}")
            
            test_data = pd.read_csv(test_data_path)
            logger.info("Test data loaded successfully")

            # Separate features and target variable
            x_test = test_data.drop(columns=[self.config.target_column])
            y_test = test_data[self.config.target_column]

            # Make predictions
            predictions = model.predict(x_test)
            logger.info("Predictions made successfully")

            # Calculate metrics
            mse = mean_squared_error(y_test, predictions)
            r2 = r2_score(y_test, predictions)
            logger.info(f"Mean Squared Error: {mse}, R^2 Score: {r2}")

            # Save metrics to a file
            metrics = {
                "mean_squared_error": mse,
                "r2_score": r2,
                "all_params": self.config.all_params
            }

            metrics_file_path = self.config.metric_file_path
            save_json(metrics_file_path, metrics)
            
            logger.info(f"Metrics saved to {metrics_file_path}")

        except Exception as e:
            logger.exception(f"Model evaluation failed with error: {e}")
            raise e
        
