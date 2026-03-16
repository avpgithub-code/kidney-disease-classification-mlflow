from pathlib import Path
import os

CONFIG_FILE_PATH = Path(r"W:\ML-DL\Repositories\kidney-disease-classification-mlflow\config\config.yaml")
PARAMS_FILE_PATH = Path(r"W:\ML-DL\Repositories\kidney-disease-classification-mlflow\params.yaml")

# CONFIG_FILE_PATH = Path(r"config\config.yaml")
# PARAMS_FILE_PATH = Path(r"params.yaml")

# # Set the custom directory to your artifacts folder
# os.environ["KAGGLEHUB_CACHE"] = config.root_dir



# path = kagglehub.dataset_download("nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone")

# # Now, any download will go into artifacts/data_ingestion
# dataset_path = kagglehub.dataset_download("username/dataset-name")

# print(f"Data is now stored in: {dataset_path}")

# Kaggle API Token: 1c8e
# KGAT_b455a195c1067469392c98a62166029f

# To use this token, set the KAGGLE_API_TOKEN environment variable:
# export KAGGLE_API_TOKEN=KGAT_b455a195c1067469392c98a62166029f

# After setting KAGGLE_API_TOKEN, you can use the client as follows:
# kaggle competitions list

# Set these BEFORE importing the Kaggle API
# os.environ['KAGGLE_USERNAME'] = "your_username" # Find this in your Kaggle profile
# os.environ['KAGGLE_KEY'] = "the_key_you_just_copied"

# from kaggle.api.kaggle_api_extended import KaggleApi
# api = KaggleApi()
# api.authenticate()