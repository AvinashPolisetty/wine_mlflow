import os
import yaml
from box.exceptions import BoxValueError
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from src.mlproject import logging


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} is loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    try:
        for path in path_to_directories:
            os.makedirs(path,exist_ok=True)
            if verbose:
                logging.info(f"created directory:{path}")
    except Exception as e:
        raise e 
    

@ensure_annotations
def get_size(path:Path): 
    size=round(os.path.getsize(path)/1024)
    return  f"~ {size} KB"


@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as file_obj:
        json.dump(data,file_obj,indent=4)
    logging.info(f'file saved at {path}')


@ensure_annotations 
def load_json(path:Path):
    with open(path) as f:
        data=json.load(f)

    logging.info(f"json file loaded successfully from :{path}")
    return ConfigBox(data)


@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")



@ensure_annotations
def load_bin(path:Path)->Any:
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data



