from gtts import gTTS
from io import BytesIO
import streamlit as st

st.title("🔊 Pronunciation Practice")

word = st.text_input("Enter a word to hear it:")

if word:
    tts = gTTS(word)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)  
    st.audio(audio_fp, format="audio/mp3")  
