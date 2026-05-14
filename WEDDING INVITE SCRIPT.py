import streamlit as st
from PIL import Image
import random
import base64

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Manish Weds Mansi",
    page_icon="💍",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"] {
    background: linear-gradient(to bottom, #fff5e6, #ffe6e6);
    font-family: Georgia;
}

/* Mobile Friendly */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 700px;
}

/* Title */
.title {
    text-align:center;
    font-size:42px;
    color:#8B0000;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#b8860b;
    font-size:24px;
    margin-bottom:20px;
}

/* Buttons */
.stButton>button {
    width:100%;
    border-radius:12px;
    background-color:#8B0000;
    color:white;
    font-size:18px;
    border:none;
    padding:0.6rem;
}

/* Flower Animation */

.flower {
    position: fixed;
    top: -10vh;
    animation: fall linear infinite;
    z-index: 999;
}

.flower:nth-child(1) {
    left: 10%;
    animation-duration: 10s;
}

.flower:nth-child(2) {
    left: 30%;
    animation-duration: 14s;
}

.flower:nth-child(3) {
    left: 50%;
    animation-duration: 12s;
}

.flower:nth-child(4) {
    left: 70%;
    animation-duration: 15s;
}

.flower:nth-child(5) {
    left: 90%;
    animation-duration: 13s;
}

@keyframes fall {
    0% {
        transform: translateY(-10vh) rotate(0deg);
    }

    100% {
        transform: translateY(110vh) rotate(360deg);
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- FLOWERS ---------------- #

st.markdown("""
<div class="flower">🌸</div>
<div class="flower">🌺</div>
<div class="flower">💮</div>
<div class="flower">🏵️</div>
<div class="flower">🌼</div>
""", unsafe_allow_html=True)

# ---------------- TITLES ---------------- #

st.markdown('<div class="title">💍 शुभ विवाह 💍</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Manish ❤️ Mansi</div>',
    unsafe_allow_html=True
)

# ---------------- MUSIC PLAYER ---------------- #

music_files = [
    "jashne_bahara.mp3",
    "mangalyam_sathiya.mp3"
]

audio_html = f"""
<audio id="weddingMusic" autoplay controls style="width:100%;">
    <source src="{random.choice(music_files)}" type="audio/mp3">
</audio>

<script>

const songs = {music_files};

let currentSong = Math.floor(Math.random() * songs.length);

const player = document.getElementById("weddingMusic");

player.src = songs[currentSong];

player.addEventListener('ended', function() {{

    currentSong++;

    if(currentSong >= songs.length){{
        currentSong = 0;
    }}

    player.src = songs[currentSong];

    player.play();

}});

</script>
"""

st.markdown(audio_html, unsafe_allow_html=True)

# ---------------- IMAGE PAGES ---------------- #

pages = [
    "page_1.jpg",
    "page_2.jpg",
    "page_3.jpg"
]

if "page" not in st.session_state:
    st.session_state.page = 0

# ---------------- NAVIGATION ---------------- #

col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("⬅ Previous"):
        if st.session_state.page > 0:
            st.session_state.page -= 1

with col2:
    st.markdown(
        f"<h3 style='text-align:center;color:#8B0000;'>Page {st.session_state.page+1}/{len(pages)}</h3>",
        unsafe_allow_html=True
    )

with col3:
    if st.button("Next ➡"):
        if st.session_state.page < len(pages)-1:
            st.session_state.page += 1

# ---------------- DISPLAY IMAGE ---------------- #

image = Image.open(pages[st.session_state.page])

st.image(image, use_container_width=True)

# ---------------- FOOTER ---------------- #

st.markdown(
    "<h4 style='text-align:center;color:#8B0000;'>✨ With Love & Blessings ✨</h4>",
    unsafe_allow_html=True
)
