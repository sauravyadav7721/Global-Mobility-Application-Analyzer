import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from visa.entity.config_entity import DataIngestionConfig
from visa.entity.artifact_entity import DataIngestionArtifact
from visa.exception import USvisaException
from visa.logger import logging
from visa.data_access.visa_data import VisaData

class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig=DataIngestionConfig()):
        try:
            
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise USvisaException(e, sys)
        
    def export_data_into_feature_store(self) -> DataFrame:
        try:
            logging.info(f"Exporting collection data as dataframe")
            usvisa_data = VisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=
                                                                   self.data_ingestion_config.collection_name)
            logging.info(f"Exported collection data as dataframe with shape: {dataframe.shape}")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Saving dataframe to feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        
        except Exception as e:
            raise USvisaException(e, sys)
        
    def split_data_as_train_test(self, dataframe: DataFrame) -> None:

        logging.info(f"Entered split_data_as_train_test method of DataIngestion class.")

        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42)
            logging.info(f"Performed train test split on the dataframe")
            logging.info("Exited split_data_as_train_test method of DataIngestion class.")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"EXporting train and test file to respective file paths")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info(f"Exported train and test file to respective file paths")
        except Exception as e:
            raise USvisaException(e, sys) from e
        

    def initiate_data_ingestion(self) -> DataIngestionArtifact:

        logging.info("Entered initiate_data_ingestion method")

        try:
            dataframe = self.export_data_into_feature_store()

            logging.info("Got data from MongoDB")

            self.split_data_as_train_test(dataframe=dataframe)

            logging.info("Performed train-test split")

            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )

            logging.info("Created data ingestion artifact")

            return data_ingestion_artifact

        except Exception as e:
            raise USvisaException(e, sys) from e
            
                