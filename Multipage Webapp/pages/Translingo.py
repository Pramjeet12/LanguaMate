import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit UI
st.title("Text Translator")
st.write("Enter text to translate into another language.")

# Input text
text_to_translate = st.text_area("Enter the text", height=100)

# Select target language
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Chinese (Traditional)": "zh-tw",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Swedish": "sv",
    "Danish": "da",
    "Norwegian": "no",
    "Finnish": "fi",
    "Turkish": "tr",
    "Arabic": "ar",
    "Hindi": "hi",
    "Thai": "th",
    "Vietnamese": "vi",
    "Hebrew": "he",
    "Indonesian": "id",
    "Malay": "ms",
    "Czech": "cs",
    "Hungarian": "hu",
    "Romanian": "ro",
    "Bulgarian": "bg",
    "Ukrainian": "uk",
    "Slovak": "sk",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Estonian": "et",
}

target_language = st.selectbox("Select target language:", list(languages.keys()))

if st.button("Translate"):
    if text_to_translate:
        # Translate the text
        translated = GoogleTranslator(source='auto', target=languages[target_language]).translate(text_to_translate)
        st.write("Translation:", translated)
    else:
        st.error("Please enter some text to translate.")



st.markdown("---")  # Adds a horizontal line
if st.button("About the Developer"):
    st.write("Created by: Kumar")  # Replace with your name

