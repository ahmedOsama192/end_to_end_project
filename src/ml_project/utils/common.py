

import os 
from box.exceptions import BoxValueError
from src import logger
import json
import yaml
from typing import Any, Dict, Union
from box import config_box
from pathlib import Path
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(file_path: Union[str, Path]) -> config_box :

    """
    Reads a YAML file and returns its content as a Box object.
    
    Args:
        file_path (Union[str, Path]): The path to the YAML file.
        
    Returns:
        config_box: A Box object containing the YAML file's content.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f"YAML file '{file_path}' read successfully.")
            return config_box(data)
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}")
        raise e
    
    except yaml.YAMLError as e:
        logger.error(f"Error reading YAML file: {file_path}")
        raise e
    
    except BoxValueError as e:
        logger.error(f"Error converting YAML to Box: {e}")
        raise e

@ensure_annotations
def read_json(file_path: Union[str, Path]) -> Dict[str, Any]:

    """
    Reads a JSON file and returns its content as a dictionary.
    
    Args:
        file_path (Union[str, Path]): The path to the JSON file.
        
    Returns:
        Dict[str, Any]: A dictionary containing the JSON file's content.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logger.info(f"JSON file '{file_path}' read successfully.")
            return config_box(data)
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {file_path}")
        raise e
    
    except json.JSONDecodeError as e:
        logger.error(f"Error reading JSON file: {file_path}")
        raise e

@ensure_annotations
def save_json(file_path: Union[str, Path], data: Dict[str, Any]) -> None:
    """
    Saves a dictionary to a JSON file.
    
    Args:
        file_path (Union[str, Path]): The path to the JSON file.
        data (Dict[str, Any]): The data to save.
        
    Returns:
        None
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logger.info(f"Data saved to JSON file '{file_path}' successfully.")
            
    except IOError as e:
        logger.error(f"Error writing to JSON file: {file_path}")
        raise e

@ensure_annotations
def save_yaml(file_path: Union[str, Path], data: config_box) -> None:
    """
    Saves a Box object to a YAML file.
    
    Args:
        file_path (Union[str, Path]): The path to the YAML file.
        data (config_box): The data to save.
        
    Returns:
        None
    """
    try:
        with open(file_path, 'w') as file:
            yaml.safe_dump(data.to_dict(), file)
            logger.info(f"Data saved to YAML file '{file_path}' successfully.")
            
    except IOError as e:
        logger.error(f"Error writing to YAML file: {file_path}")
        raise e

@ensure_annotations
def create_directory(directory: Union[str, Path]) -> None:
    """
    Creates a directory if it does not exist.
    
    Args:
        directory (Union[str, Path]): The path to the directory.
        
    Returns:
        None
    """
    try:
        os.makedirs(directory, exist_ok=True)
        logger.info(f"Directory '{directory}' created or already exists.")
        
    except OSError as e:
        logger.error(f"Error creating directory: {directory}")
        raise e
    