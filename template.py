import os
from pathlib import Path
import logging

#logging String
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "cnnClassifier"
list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constants.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
    "main.py",
    "research/trials.ipynb",
    "templates/index.html" 
]
for file in list_of_file:
    file_path = Path(file)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info("Creating directory: %s", file_dir)
    if not (os.path.exists(file_path)) or (os.path.getsize(file_path)) == 0:
        with open(file_path, "w",encoding="utf-8") as f:
            pass
        logging.info("Creating file: %s", file_path)
    else:
        logging.info("File already exists: %s", file_path)