from src.mlproject.constants import *
from src.mlproject.utils.common import read_yaml,create_directories
from src.mlproject.entity.config_entity import (DataIngestionConfig,DataValidationConfig,DataTransformartionConfig,
                                                ModelTrainingConfig,ModelEvaluationConfig)


class ConfigurationManager:
    def __init__(self,
                config_filepath=CONFIG_FILE_PATH,
                params_filepath=PARAMS_FILE_PATH,
                schema_filepath=SCHEMA_FILE_PATH):

        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_valiation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_dir=config.unzip_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    
    def get_data_transform_config(self)->DataTransformartionConfig:
        config=self.config.data_transformation

        create_directories([config.root_dir])

        data_transform_config=DataTransformartionConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        
        return data_transform_config

    
    def get_model_train_config(self)->ModelTrainingConfig:
        config=self.config.model_trainer
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN

        create_directories([config.root_dir])
        
        model_train_config=ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )

        return model_train_config
    


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/aviavinashp64/wine_mlflow.mlflow"
        )

        return model_evaluation_config
    
