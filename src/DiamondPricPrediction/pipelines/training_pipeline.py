import pandas as pd
import numpy as np
import os
import sys
from src.DiamondPricPrediction.logger import logging
from src.DiamondPricPrediction.exception import customexception
from src.DiamondPricPrediction.components.data_ingestion import DataIngestion

obj = DataIngestion()

obj.initiate_data_ingestion()