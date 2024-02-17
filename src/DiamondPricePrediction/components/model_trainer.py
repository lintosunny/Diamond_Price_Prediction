import pandas as pd
import numpy as np
import os
import sys
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import customexception
from dataclasses import dataclass
from src.DiamondPricePrediction.utils.utils import save_object
from src.DiamondPricePrediction.utils.utils import evaluate_model

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_data_training(self, train_array, test_array):

        try:
            logging.info('Spliting dependent and independent variables from test and train data')

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1], 
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'Linear Regression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'ElasticNet':ElasticNet()
            }


            model_report:dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print('\n==================================================================\n')
            logging.info(f'Model Report: {model_report}')

            # To get best model score from dictionary
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            print(f'Best model found, Mode Name: {best_model}, R2 score: {best_model_score}')
            print('\n====================================================================\n')
            logging.info(f'Best model found, Mode Name: {best_model}, R2 score: {best_model_score}' )

            save_object(
                self.model_trainer_config.trained_model_file_path,
                best_model
            )

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise customexception(e, sys)
        
