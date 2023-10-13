from src.mlproject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage03_data_transformation import DataTransformationTrainigPipeline
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
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


Stage_name="Data Transformation"

try:
    logging.info(f">>>>>> {Stage_name} started <<<<<<<<<")
    data_ingestion=DataTransformationTrainigPipeline()
    data_ingestion.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


