# Genderize

Genderize is an application that detects faces from an image file, classifies them according to gender (male/female) and
creates a dataset of images properly classified under folders for each gender.

## Requirements

### Python3
Before running the program, install Python 3.6:
* On Linux, open terminal and type: 
  ```
  sudo apt-get update
  sudo apt-get install python3.6
  ```
* [Anaconda](https://www.continuum.io/downloads) provides Python3.6 for Windows, macOS, and Linux too.

### OpenCV
Once you have Python3.6 installed, type the following commands:
```
pip3 install opencv-python
pip3 install opencv-contrib-python
```

## Running the Program
Run genderize.py with the command `python facifier.py` and pass the path to the image from which you want to extract faces from as an argument.


Example:
```
python facifier.py dataset_img/QgqFDU7RfxtFx1AL.png
```