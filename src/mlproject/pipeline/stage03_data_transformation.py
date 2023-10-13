from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_transformation import DataTransformation
from pathlib import Path


class DataTransformationTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            
            if status=="True":

                config=ConfigurationManager()
                data_transform_config=config.get_data_transform_config()
                data_transformation=DataTransformation(config=data_transform_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("data schema is not valid")
            
        except Exception as e:
            raise e