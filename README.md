Image Transformation App
This is a Stremlit application that allows users to apply various affine transformations to images. The app is built using Streamlit and provides an intuitive interface for uploading an image, selecting a transformation, and viewing the results.

Features
The app supports the following image transformations:

1. Translation: Shift the image horizontally and/or vertically.
2. Rotation: Rotate the image by a specified angle.
3. Scaling: Resize the image with customizable scaling factors.
4. Shearing: Apply a shearing effect to the image.

How to Use
1. Upload an Image: Use the "Upload an Image" section to select an image (JPG, JPEG, or PNG).
2. Select a Transformation: Choose from Translation, Rotation, Scaling, or Shearing.
3. Adjust Parameters: Use sliders to set parameters like translation distance, rotation angle, scaling factors, or shear values.
4. View Transformed Image: Click the Apply button to see the transformed image.
5. Download Result (optional): Save the transformed image using your browser.

Setup for Local Deployment
Follow these steps to run the app locally:

1. Clone this repository:

git clone https://github.com/PratikYelkar/CV-ASS.git
cd image-transformation-app

2. Install dependencies:

 pip install -r requirements.txt

3. Run the Streamlit app:

 streamlit run streamlit_app.py

4. Open the app in your browser at (https://htjvaemunt8bx8ymxscqbt.streamlit.app/).

Technologies Used
1. Streamlit: For building the interactive web app.
2. OpenCV: For performing image transformations.
3. Pillow: For image handling and processing.
4. NumPy: For numerical operations.




