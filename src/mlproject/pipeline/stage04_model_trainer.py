from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_trainer import ModelTraining 


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_train_config()
            model_trainer_config = ModelTraining(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e