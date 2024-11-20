import cv2
import numpy as np

def translate_image(image, tx, ty):
    rows, cols = image.shape[:2]
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, translation_matrix, (cols, rows))

def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(image, rotation_matrix, (cols, rows))

def scale_image(image, scale_x, scale_y):
    rows, cols = image.shape[:2]
    scaling_matrix = np.float32([[scale_x, 0, 0], [0, scale_y, 0]])
    return cv2.warpAffine(image, scaling_matrix, (int(cols * scale_x), int(rows * scale_y)))

def shear_image(image, shear_x, shear_y):
    rows, cols = image.shape[:2]
    shear_matrix = np.float32([[1, shear_x, 0], [shear_y, 1, 0]])
    return cv2.warpAffine(image, shear_matrix, (cols, rows))
