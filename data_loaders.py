# data_loaders.py
from pathlib import Path
import logging
import pandas as pd
import json
import yaml

# Do not call logging.basicConfig() here.
# Use the logging configuration from Part 1.
logger = logging.getLogger(__name__)

def load_csv(filepath):
    """Load a CSV file into a pandas DataFrame."""
    data = pd.read_csv(filepath)
    logger.info(f"Loaded CSV file: {filepath} ({len(data)} rows)")
    return data

def load_json(filepath):
    """Load a JSON file into a Python object."""
    with open(filepath, "r") as file:
        data = json.load(file)
    logger.info(f"Loaded JSON file: {filepath}")
    return data

def load_yaml(filepath):
    """Load a YAML file into a Python object."""
    with open(filepath, "r") as file:
        data = yaml.safe_load(file)

    logger.info(f"Loaded YAML file: {filepath}")
    return data