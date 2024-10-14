import streamlit as st
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import cv2
from PIL import Image
import numpy as np





# Set up the Streamlit app title
st.title("Text Extraction from Images")



# File uploader for image files
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)

    # Convert the image to an OpenCV format
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Perform OCR on the image
    text = pytesseract.image_to_string(img)

    # Display the image and the extracted text
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.subheader("Extracted Text:")
    st.write(text)