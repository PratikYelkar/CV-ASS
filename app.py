import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to translate the image
def translate_image(image, tx, ty):
    """Translate the image by tx and ty."""
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    translated = cv2.warpAffine(image, M, (cols, rows))
    return translated

# Function to rotate the image
def rotate_image(image, angle):
    """Rotate the image by a specified angle."""
    rows, cols = image.shape[:2]
    center = (cols // 2, rows // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    rotated = cv2.warpAffine(image, M, (cols, rows))
    return rotated

# Function to scale the image
def scale_image(image, fx, fy):
    """Scale the image by fx and fy."""
    scaled = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled

# Function to shear the image
def shear_image(image, shear_factor, axis="x"):
    """Shear the image along the specified axis."""
    rows, cols = image.shape[:2]
    if axis == "x":
        M = np.float32([[1, shear_factor, 0], [0, 1, 0]])
    elif axis == "y":
        M = np.float32([[1, 0, 0], [shear_factor, 1, 0]])
    else:
        raise ValueError("Axis must be 'x' or 'y'.")
    sheared = cv2.warpAffine(image, M, (cols, rows))
    return sheared

# Function to display images in Streamlit
def display_images(images, titles):
    """Display images in a grid using Streamlit."""
    cols = st.columns(len(images))
    for i, col in enumerate(cols):
        col.image(images[i], caption=titles[i], use_column_width=True)

# Streamlit app setup
st.title("Image Transformation App")
st.write("Upload an image to apply various affine transformations.")

# File uploader in Streamlit
uploaded_file = st.file_uploader("D:\VS Code\Computer Vision\CV\IMG\cristino.jpg", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = np.array(Image.open(uploaded_file))

    # Sidebar parameters for transformations
    st.sidebar.header("Transformation Parameters")
    tx = st.sidebar.slider("Translation - X", -100, 100, 50)
    ty = st.sidebar.slider("Translation - Y", -100, 100, 30)
    angle = st.sidebar.slider("Rotation Angle", -180, 180, 45)
    fx = st.sidebar.slider("Scaling Factor - X", 0.5, 2.0, 1.5)
    fy = st.sidebar.slider("Scaling Factor - Y", 0.5, 2.0, 1.5)
    shear_factor = st.sidebar.slider("Shear Factor", -1.0, 1.0, 0.3)
    axis = st.sidebar.selectbox("Shear Axis", ["x", "y"])

    # Apply transformations
    translated_image = translate_image(image, tx=tx, ty=ty)
    rotated_image = rotate_image(image, angle=angle)
    scaled_image = scale_image(image, fx=fx, fy=fy)
    sheared_image = shear_image(image, shear_factor=shear_factor, axis=axis)

    # Display the original and transformed images
    images = [image, translated_image, rotated_image, scaled_image, sheared_image]
    titles = ["Original", "Translated", "Rotated", "Scaled", "Sheared"]
    display_images(images, titles)
