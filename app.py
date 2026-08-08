import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Text to Speech", page_icon="🔊")

st.title("Text to Speech Converter 🔊")
st.write("Paste your paragraph below to generate an MP3.")

# Text area for user input
text_input = st.text_area("Enter text here:", height=250)

if st.button("Convert to MP3"):
    if text_input.strip():
        with st.spinner("Converting text to audio..."):
            # Convert text to speech
            tts = gTTS(text=text_input, lang='en', slow=False)
            audio_file = "output.mp3"
            tts.save(audio_file)

            st.success("Conversion successful!")

            # Play the audio directly in the web app
            st.audio(audio_file, format="audio/mp3")

            # Create a download button for the MP3
            with open(audio_file, "rb") as file:
                st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name="audio_speech.mp3",
                    mime="audio/mp3"
                )
    else:
        st.warning("Please enter some text before converting.")