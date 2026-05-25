import os
import sys
import yaml
from src.exception import MyException
from src.logger import logging
from box import ConfigBox
import json
from pathlib import Path
import base64


def read_yaml(file_path:str):
    try:
        with open(file_path, 'rb') as yaml_file:
            return ConfigBox(yaml.safe_load(yaml_file))
    except Exception as e:
        raise MyException(e, sys)
    
def create_directories(path_to_directories:list):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)


def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()