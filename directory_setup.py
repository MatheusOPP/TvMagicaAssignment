from settings import *
from pathlib import Path

def directory_setup():
    """Set up directories if they don't exist"""
    Path(IMAGE_OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)
    for gender in GENDER_LIST:
        (Path(IMAGE_OUTPUT_FOLDER) / gender).mkdir(parents=True, exist_ok=True)
