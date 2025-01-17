import streamlit as st
from googletrans import Translator
translator = Translator ()
language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    'la': "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}
def translate_text (text, dest):
    try:
        
        translated = translator. translate (text, dest=dest)
        st. write(f"\n{language[dest]} translation: {translated.text}")
        if translated. pronunciation:
            st. write (f"Pronunciation: {translated. pronunciation}")
        

        else:
            st. write ("Pronunciation not available")
            source_lang = language.get(translated.src)
            if source_lang:
                st. write (f"Translated from : {source_lang}")
            else:
                st. write ("Source language unknown")
    except Exception as e:
        st. error ("Translation failed: " + str(e))
def main ():
    st. title ("Language Translator")
    dest_language = st. selectbox ("Select Destination Language", options=list(language))
    text = st.text_area ("Enter text to translate")
    if st. button("Translate"):
        translate_text (text, dest_language)
        if __name__ == "__main__":
            main ()