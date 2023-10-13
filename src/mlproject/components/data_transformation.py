import os
import pandas as pd
from src.mlproject import logging
from sklearn.model_selection import train_test_split
from src.mlproject.entity.config_entity import DataTransformartionConfig




class DataTransformation:
    def __init__(self,config=DataTransformartionConfig):
        self.config=config

    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        #train test split
        train,test=train_test_split(data,test_size=0.2)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        
        logging.info("Splited data into training and test sets")
        logging.info(train.shape)
        logging.info(test.shape)

        print(train.shape)
        print(test.shape)
        
        
        