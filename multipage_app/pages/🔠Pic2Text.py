import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np

# Configure tesseract path if needed (for local development)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Streamlit app title
st.title("Text Extraction from Images")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Convert to OpenCV format
    img = np.array(image)
    
    # Preprocess image for better OCR results
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Apply threshold to get better text recognition
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    try:
        # Extract text using pytesseract
        extracted_text = pytesseract.image_to_string(thresh, config='--psm 6')
        
        # Display extracted text
        if extracted_text.strip():
            st.subheader("Extracted Text:")
            st.text_area("", value=extracted_text, height=100)
        else:
            st.write("No text found.")
    except Exception as e:
        st.error(f"Error extracting text: {str(e)}")
