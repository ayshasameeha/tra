# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OQAgOVqQyZsill7npvfhS7z2XsI_PHuJ
"""

import streamlit as st
from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Streamlit app title
st.title("Language Translator")

# Input text
input_text = st.text_area("Enter text to translate:")

# Language selection
from_lang = st.selectbox("Select source language:", translator.LANGUAGES.keys())
to_lang = st.selectbox("Select target language:", translator.LANGUAGES.keys())

# Translate button
if st.button("Translate"):
    try:
        # Translate the input text
        translated_text = translator.translate(input_text, src=from_lang, dest=to_lang).text
        st.success("Translation:")
        st.write(translated_text)
    except Exception as e:
        st.error("An error occurred while translating. Please try again.")

# Display information about the supported languages
st.sidebar.subheader("Supported Languages")
st.sidebar.write(translator.LANGUAGES)