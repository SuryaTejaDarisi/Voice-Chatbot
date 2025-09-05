import streamlit as st
from streamlit_mic_recorder import speech_to_text
import google.generativeai as genai
from gtts import gTTS
import markdown
import re
import tempfile
import os


GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)


# Initialization
if "history" not in st.session_state:
    st.session_state.history = []

st.title("Voice Chatbot for Creative Cartels")

# Speech to Text
st.write("How can I help you today ?")
st.write("Click on the Mic to ask something.")
spoken_text = speech_to_text(language='en', use_container_width=True, key=f"stt_{len(st.session_state.history)}")

if spoken_text:
    st.markdown(f"{spoken_text}")
    st.session_state.history.append({"role": "user", "content": spoken_text})

    with st.spinner("Be cool while we generate a response for you !!!"):
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(spoken_text)
        reply = response.text if hasattr(response, 'text') else str(response)
    st.markdown(f"{reply}")
    st.session_state.history.append({"role": "assistant", "content": reply})

    # Text to Speech
    html = markdown.markdown(reply)
    cleanedText = re.sub('<[^<]+?>', '', html)
    tts = gTTS(cleanedText, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format='audio/mp3')
        audio_path = fp.name

# Previously Asked Questions
if st.session_state.history:
    st.markdown("---")
    st.write("**Past Conversations**")
    for h in st.session_state.history:
        if h["role"] == "user":
            st.write(f"**{h['content']}**")
        else:
            st.write("**Response:**")
            st.write(f"{h['content']}")