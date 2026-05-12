import os
import sys
import yaml
from src.exception import MyException
from src.logger import logging
from box import ConfigBox

def read_yaml(file_path:str):
    try:
        with open(file_path, 'rb') as yaml_file:
            return ConfigBox(yaml.safe_load(yaml_file))
    except Exception as e:
        raise MyException(e, sys)
    
def create_directories(path_to_directories:list):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
