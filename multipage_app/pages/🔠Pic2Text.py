import streamlit as st
import easyocr
from PIL import Image

# Initialize EasyOCR reader
reader = easyocr.Reader(['en', 'es', 'fr', 'de'])  # Add more languages as needed

# Streamlit app title
st.title("Text Extraction from Images")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extract text from image

    result = reader.readtext(image)

    # Display extracted text
    if result:
        st.subheader("Extracted Text:")
        extracted_text = " ".join([text for (_, text, _) in result])
        st.text_area("", value=extracted_text, height=100)
    else:
        st.write("No text found.")

