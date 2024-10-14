import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# Set up the Streamlit app title
st.title("Text Extraction from Images")

# Initialize the EasyOCR reader with multiple languages
# Example: English ('en'), Spanish ('es'), French ('fr'), and German ('de')
reader = easyocr.Reader(['en', 'es', 'fr', 'de', 'it', 'pt', 'zh', 'ja', 'ko'])

# File uploader for image files
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)

    # Convert the image to a NumPy array
    img = np.array(image)

    # Perform OCR on the image
    result = reader.readtext(img)

    # Extract text from the result
    extracted_text = "\n".join([text[1] for text in result])

    # Display the image and the extracted text
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.subheader("Extracted Text:")
    st.write(extracted_text)
