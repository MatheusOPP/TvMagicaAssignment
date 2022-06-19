# Import Libraries
import cv2
import numpy as np
from predict_gender import generate_gendered_images
from settings import *
import uuid
from pathlib import Path

# load face Caffe model
face_net = cv2.dnn.readNetFromCaffe(FACE_PROTO, FACE_MODEL)
# Load gender prediction model
gender_net = cv2.dnn.readNetFromCaffe(GENDER_MODEL, GENDER_PROTO)

if __name__ == "__main__":
    # Parsing command line arguments entered by user
    import sys

    generate_gendered_images(sys.argv[1], face_net, gender_net)
