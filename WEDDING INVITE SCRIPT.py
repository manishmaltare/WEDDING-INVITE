import streamlit as st
import streamlit.components.v1 as components

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Wedding Invitation",
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
    background-color: #fffaf5;
    font-family: Georgia;
}

/* Reduce top spacing */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 650px;
}

/* Title */
.title {
    text-align:center;
    font-size:38px;
    color:#8B0000;
    font-weight:bold;
    margin-bottom:0px;
}

.subtitle {
    text-align:center;
    font-size:20px;
    color:#b8860b;
    margin-bottom:15px;
}

/* Buttons */
.stButton>button {
    width:100%;
    border-radius:10px;
    background-color:#8B0000;
    color:white;
    border:none;
    padding:0.45rem;
    font-size:16px;
    font-weight:bold;
}

.stButton>button:hover {
    background-color:#a50000;
    color:white;
}

/* Flowers Animation */
.flower {
    position: fixed;
    top: -10vh;
    animation: fall linear infinite;
    z-index: 999;
    opacity:0.8;
}

.flower:nth-child(1){
    left:10%;
    animation-duration:10s;
}

.flower:nth-child(2){
    left:30%;
    animation-duration:13s;
}

.flower:nth-child(3){
    left:50%;
    animation-duration:11s;
}

.flower:nth-child(4){
    left:70%;
    animation-duration:14s;
}

.flower:nth-child(5){
    left:90%;
    animation-duration:12s;
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
<div class="flower">🏵️</div>
<div class="flower">💮</div>
<div class="flower">🌼</div>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.markdown(
    '<div class="title">💍 शुभ विवाह 💍</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Manish ❤️ Mansi</div>',
    unsafe_allow_html=True
)

# ---------------- MUSIC PLAYER ---------------- #

music_html = """
<!DOCTYPE html>
<html>
<body>

<audio id="music" autoplay controls style="width:100%;">
</audio>

<script>

var songs = [
    "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/main/jashne_bahara.mp3",
    
    "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/main/mangalyam_sathiya.mp3"
];

var current = 0;

var music = document.getElementById("music");

function playSong(index){

    music.src = songs[index];

    music.play();

}

playSong(current);

music.addEventListener("ended", function(){

    current++;

    if(current >= songs.length){
        current = 0;
    }

    playSong(current);

});

</script>

</body>
</html>
"""

components.html(music_html, height=70)

# ---------------- PAGE LIST ---------------- #

pages = [
    "page_1.jpg",
    "page_2.jpg",
    "page_3.jpg"
]

# ---------------- SESSION ---------------- #

if "page" not in st.session_state:
    st.session_state.page = 0

# ---------------- NAVIGATION ---------------- #

col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("⬅"):
        if st.session_state.page > 0:
            st.session_state.page -= 1

with col2:
    st.markdown(
        f"<h4 style='text-align:center;color:#8B0000;'>Page {st.session_state.page+1}/{len(pages)}</h4>",
        unsafe_allow_html=True
    )

with col3:
    if st.button("➡"):
        if st.session_state.page < len(pages)-1:
            st.session_state.page += 1

# ---------------- SHOW IMAGE ---------------- #

st.image(
    pages[st.session_state.page],
    use_container_width=True
)

# ---------------- FOOTER ---------------- #

st.markdown(
    "<div style='text-align:center;color:#8B0000;font-size:18px;'>✨ Welcome With Love ✨</div>",
    unsafe_allow_html=True
)
