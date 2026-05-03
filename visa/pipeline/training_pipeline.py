import sys
from visa.exception import USvisaException
from visa.logger import logging
from visa.components.data_ingestion import DataIngestion

from visa.entity.config_entity import DataIngestionConfig
from visa.entity.artifact_entity import DataIngestionArtifact

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(f"Entered the start_data_ingestion method of TrainingPipeline class.") 
            logging.info(f"Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train and test file path.")
            logging.info(f"Exited the start_data_ingestion method of TrainingPipeline class.")
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e, sys) from e
        


    def run_pipeline(self, ) ->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise USvisaException(e, sys) from e