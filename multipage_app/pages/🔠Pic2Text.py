import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
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
    
    # Preprocess image for better OCR results using PIL
    # Convert to grayscale
    if image.mode != 'L':
        gray_image = image.convert('L')
    else:
        gray_image = image
    
    # Enhance contrast and sharpness
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(2.0)
    
    # Apply sharpening filter
    sharpened_image = enhanced_image.filter(ImageFilter.SHARPEN)
    
    try:
        # Extract text using pytesseract
        extracted_text = pytesseract.image_to_string(sharpened_image, config='--psm 6')
        
        # Display extracted text
        if extracted_text.strip():
            st.subheader("Extracted Text:")
            st.text_area("", value=extracted_text, height=100)
        else:
            st.write("No text found.")
    except Exception as e:
        st.error(f"Error extracting text: {str(e)}")
