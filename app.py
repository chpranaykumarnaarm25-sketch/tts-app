import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Text to Speech", page_icon="🔊")

st.title("Text to Speech Converter 🔊")
st.write("Paste your paragraph below to generate an MP3.")

# Dropdown for accents
accent = st.selectbox(
    "Select an English Accent:", 
    ["American", "British", "Indian", "Australian"]
)

# Text area for user input
text_input = st.text_area("Enter text here:", height=250)

# Map the selected accent to the correct Google domain
tld_map = {
    "American": "com",
    "British": "co.uk",
    "Indian": "co.in",
    "Australian": "com.au"
}

if st.button("Convert to MP3"):
    if text_input.strip():
        with st.spinner("Converting text to audio..."):
            selected_tld = tld_map[accent]
            
            # Convert text to speech using the selected accent
            tts = gTTS(text=text_input, lang='en', tld=selected_tld, slow=False)
            audio_file = "output.mp3"
            tts.save(audio_file)
            
            st.success("Conversion successful!")
            
            # Play the audio
            st.audio(audio_file, format="audio/mp3")
            
            # Download button
            with open(audio_file, "rb") as file:
                st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name="audio_speech.mp3",
                    mime="audio/mp3"
                )
    else:
        st.warning("Please enter some text before converting.")
