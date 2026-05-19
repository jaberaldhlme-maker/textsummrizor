import os
from box.exceptions import BoxValueError
from textSummarizer.logging import logger
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:

        path_to_yaml (Path): The path to the YAML file.

        """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError(f"Error converting YAML content to ConfigBox: {e}")
    except Exception as e:
        raise ValueError(f"Error reading YAML file {path_to_yaml}: {e}")
    

    def create_directories(path_to_directories: list) -> None:
        """
        Creates directories if they do not exist.

        Args:
            path_to_directories (list): A list of directory paths to create.
        """
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            logger.info(f"Directory {path} created successfully or already exists.")