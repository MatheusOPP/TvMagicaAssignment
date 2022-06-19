# Import Libraries
import cv2
import numpy as np
from image import display_img, image_resize, get_optimal_font_scale
from face_detection import get_faces
from settings import *
from directory_setup import directory_setup


def predict_gender(input_path: str, face_net, gender_net):
    """Predict the gender of the faces showing in the image"""
    # Read Input Image
    img = cv2.imread(input_path)
    # resize the image, uncomment if you want to resize the image
    # img = cv2.resize(img, (frame_width, frame_height))
    # Take a copy of the initial image and resize it
    frame = img.copy()
    # if frame.shape[1] > frame_width:
    #     frame = image_resize(frame, width=frame_width)
    # predict the faces
    faces = get_faces(frame, face_net)
    # Loop over the faces detected
    # for idx, face in enumerate(faces):
    face_data = []
    for i, (start_x, start_y, end_x, end_y) in enumerate(faces):
        face_img = frame[start_y:end_y, start_x:end_x]
        # image --> Input image to preprocess before passing it through our dnn for classification.
        # scale factor = After performing mean substraction we can optionally scale the image by some factor. (if 1 -> no scaling)
        # size = The spatial size that the CNN expects. Options are = (224*224, 227*227 or 299*299)
        # mean = mean substraction values to be substracted from every channel of the image.
        # swapRB=OpenCV assumes images in BGR whereas the mean is supplied in RGB. To resolve this we set swapRB to True.
        blob = cv2.dnn.blobFromImage(
            image=face_img,
            scalefactor=1.0,
            size=(227, 227),
            mean=MODEL_MEAN_VALUES,
            swapRB=False,
            crop=False,
        )
        # Predict Gender
        gender_net.setInput(blob)
        gender_preds = gender_net.forward()
        i = gender_preds[0].argmax()
        gender = GENDER_LIST[i]
        #Add to list with face data
        face_data.append({"image": face_img, "gender": gender})
    return face_data

def generate_gendered_images(input_path: str, face_net, gender_net):
    directory_setup();
    for face in predict_gender(input_path, face_net, gender_net):
        cv2.imwrite(
            "{}/{}/{}.png".format(IMAGE_OUTPUT_FOLDER, face["gender"], str(uuid.uuid4())),
            face["image"],
        )