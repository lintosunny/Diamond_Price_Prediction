import pandas as pd
import numpy as np
import os
from src.DiamondPricPrediction.logger import logging
from src.DiamondPricPrediction.exception import customexception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


class DataIngestion:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks\data", "cubic_zirconia.csv")))
            logging.info("read dataset as df")

            logging.info("performed train test split")
            train_data, test_data = train_test_split(data, test_size=0.25, random_state=3)
            logging.info("train test split completed")

        except Exception as e:
            pass