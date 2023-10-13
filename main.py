from src.mlproject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage03_data_transformation import DataTransformationTrainigPipeline
from src.mlproject.pipeline.stage04_model_trainer import ModelTrainingPipeline
from src.mlproject.pipeline.stage05_model_evaluation import ModelEvaluationPipeline
from src.mlproject import logging

Stage_name="Data Ingestion"

try:
    logging.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


Stage_name="Data Validation"

try:
    logging.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


Stage_name="Data Transformation"

try:
    logging.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_transform=DataTransformationTrainigPipeline()
    data_transform.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


Stage_name="Model Training"

try:
    logging.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    model_train=ModelTrainingPipeline()
    model_train.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


Stage_name="Model Training"

try:
    logging.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    model_evaluation=ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


