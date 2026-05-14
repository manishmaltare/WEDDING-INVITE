# app.py
# Streamlit Digital Wedding Invite App
# Mobile Friendly + PDF Page Viewer + Background Music Shuffle + Indian Wedding Animations

import streamlit as st
from PIL import Image
import base64
import random
import os
from pdf2image import convert_from_path

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Manish Weds Mansi",
    page_icon="💍",
    layout="centered",
)

# ---------------- HIDE STREAMLIT DEFAULT UI ---------------- #

st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"] {
    font-family: 'Georgia', serif;
    background: linear-gradient(to bottom, #fff8f0, #ffe9d6);
}

/* Mobile Friendly */
.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
    padding-left:0.8rem;
    padding-right:0.8rem;
    max-width:700px;
}

/* Main Title */
.title-text{
    text-align:center;
    color:#8B0000;
    font-size:42px;
    font-weight:bold;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    color:#b8860b;
    font-size:20px;
    margin-bottom:25px;
}

/* Decorative Divider */
.divider{
    text-align:center;
    font-size:28px;
    color:#c99700;
    margin-top:10px;
    margin-bottom:10px;
}

/* Navigation Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    background-color:#8B0000;
    color:white;
    font-size:18px;
    border:none;
    padding:0.6rem;
    font-weight:bold;
}

.stButton>button:hover{
    background-color:#b22222;
    color:white;
}

/* Floating Flowers */
.flower{
    position: fixed;
    top:-50px;
    animation: fall linear infinite;
    z-index:999;
    opacity:0.8;
}

.flower:nth-child(1){left:10%; animation-duration:10s; font-size:22px;}
.flower:nth-child(2){left:25%; animation-duration:14s; font-size:18px;}
.flower:nth-child(3){left:40%; animation-duration:11s; font-size:24px;}
.flower:nth-child(4){left:55%; animation-duration:15s; font-size:20px;}
.flower:nth-child(5){left:70%; animation-duration:13s; font-size:26px;}
.flower:nth-child(6){left:85%; animation-duration:12s; font-size:18px;}

@keyframes fall {
    0%{
        transform: translateY(-10vh) rotate(0deg);
    }
    100%{
        transform: translateY(110vh) rotate(360deg);
    }
}

/* Glow Animation */
.glow {
  color: #8B0000;
  text-align: center;
  animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
  from {
    text-shadow: 0 0 10px #ffb347;
  }
  to {
    text-shadow: 0 0 20px #ff4500;
  }
}
</style>
""", unsafe_allow_html=True)

# ---------------- FLOWER ANIMATION ---------------- #

st.markdown("""
<div class="flower">🌸</div>
<div class="flower">🌺</div>
<div class="flower">🌼</div>
<div class="flower">💮</div>
<div class="flower">🏵️</div>
<div class="flower">🌸</div>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.markdown('<div class="title-text glow">💍 शुभ विवाह 💍</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Manish ❤️ Mansi</div>', unsafe_allow_html=True)

st.markdown('<div class="divider">✨ 🪔 ✨</div>', unsafe_allow_html=True)

# ---------------- MUSIC SHUFFLE ---------------- #

music_files = [
    "jashne_bahara.mp3",
    "mangalyam_sathiya.mp3"
]

if "music_selected" not in st.session_state:
    st.session_state.music_selected = random.choice(music_files)

selected_music = st.session_state.music_selected

def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay controls loop style="width:100%;">
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(md, unsafe_allow_html=True)

autoplay_audio(selected_music)

# ---------------- PDF TO IMAGES ---------------- #

PDF_PATH = "Wedding invite.pdf"

@st.cache_data
def load_pdf():
    pages = convert_from_path(PDF_PATH, dpi=220)
    return pages

pages = load_pdf()

# ---------------- PAGE NAVIGATION ---------------- #

if "page_num" not in st.session_state:
    st.session_state.page_num = 0

col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("⬅ Previous"):
        if st.session_state.page_num > 0:
            st.session_state.page_num -= 1

with col2:
    st.markdown(
        f"<h4 style='text-align:center;color:#8B0000;'>Page {st.session_state.page_num + 1} / {len(pages)}</h4>",
        unsafe_allow_html=True
    )

with col3:
    if st.button("Next ➡"):
        if st.session_state.page_num < len(pages)-1:
            st.session_state.page_num += 1

# ---------------- DISPLAY CURRENT PAGE ---------------- #

current_page = pages[st.session_state.page_num]

st.image(current_page, use_container_width=True)

# ---------------- FOOTER ---------------- #

st.markdown("""
<div style='text-align:center; margin-top:20px; color:#8B0000;'>
✨ With Love & Blessings ✨
</div>
""", unsafe_allow_html=True)
