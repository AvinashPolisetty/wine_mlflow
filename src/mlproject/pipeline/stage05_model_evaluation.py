from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.model_evaluation import ModelEvaluation



class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            raise e
