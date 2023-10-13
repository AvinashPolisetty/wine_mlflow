from src.mlproject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
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