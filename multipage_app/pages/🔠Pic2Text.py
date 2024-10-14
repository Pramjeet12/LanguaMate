import streamlit as st
import easyocr
from PIL import Image
import cv2
import numpy as np


# Initialize EasyOCR reader
reader = easyocr.Reader(['en', 'es', 'fr', 'de', 'it', 'nl', 'pt', 'ru', 'ch_sim', 'ja', 'ko'])
# Add more languages as needed

# Streamlit app title
st.title("Text Extraction from Images")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)


    # Convert the image to an OpenCV format
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


    # Extract text from image

    result = reader.readtext(img)

    # Display extracted text
    if result:
        st.subheader("Extracted Text:")
        extracted_text = " ".join([text for (_, text, _) in result])
        st.text_area("", value=extracted_text, height=100)
    else:
        st.write("No text found.")

