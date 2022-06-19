from settings import *
from pathlib import Path


def directory_setup(delete_old=True):
    """Set up directories for output dataset"""
    # Delete old directories if the setting for doing that is on
    output_path = Path(IMAGE_OUTPUT_FOLDER)
    if delete_old and output_path.is_dir():
        rmdir(output_path)
    # Create the directories
    output_path.mkdir(parents=True, exist_ok=True)
    for gender in GENDER_LIST:
        (output_path / gender).mkdir(parents=True, exist_ok=True)


def rmdir(directory: Path):
    """Remove directory recursively"""
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()
