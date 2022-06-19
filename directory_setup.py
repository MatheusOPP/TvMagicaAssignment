from settings import *
from pathlib import Path

def directory_setup(delete_old=True):
    """Set up directories"""
    output_path = Path(IMAGE_OUTPUT_FOLDER)
    if delete_old and output_path.is_dir():
        rmdir(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    for gender in GENDER_LIST:
        (output_path / gender).mkdir(parents=True, exist_ok=True)

def rmdir(directory: Path):
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()