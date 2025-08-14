

import pandas as pd
import os
from sklearn.linear_model import ElasticNet
from ml_project import logger
import joblib

class ModelTrainer:

    def __init__(self, config):
        self.config = config

    def train_model(self):
        try:
            # Load the training data
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)
            logger.info("Training and Testing data loaded successfully")

            # Separate features and target variable
            x_train = train_data.drop(columns=[self.config.target_column])
            y_train = train_data[self.config.target_column]
            x_test = test_data.drop(columns=[self.config.target_column])
            y_test = test_data[self.config.target_column]
            logger.info("Data separated into features and target variable")

            # Initialize the model
            model = ElasticNet(
                alpha=self.config.alpha,
                l1_ratio=self.config.l1_ratio,
                random_state=42
            )

            # Train the model
            model.fit(x_train, y_train)
            logger.info("Model training completed")

            joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
            logger.info(f"Model saved to {self.config.root_dir}/{self.config.model_name}")
        
        except Exception as e:
            logger.exception(f"Model training failed with error: {e}")
            raise e
