import streamlit as st
import streamlit.components.v1 as components

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Wedding Invitation",
    page_icon="💍",
    layout="centered"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"]{
    background:#fffaf5;
    font-family: Georgia;
}

/* Main container */
.block-container{
    padding-top:0.7rem;
    padding-bottom:0rem;
    max-width:650px;
}

/* Title */
.title{
    text-align:center;
    font-size:34px;
    color:#8B0000;
    font-weight:bold;
    margin-bottom:0px;
}

.subtitle{
    text-align:center;
    color:#b8860b;
    font-size:18px;
    margin-top:-5px;
    margin-bottom:8px;
}

/* Buttons */
.stButton > button{
    width:100%;
    border-radius:8px;
    background:#8B0000;
    color:white;
    border:none;
    padding:0.25rem;
    font-size:14px;
    font-weight:bold;
    min-height:35px;
}

.stButton > button:hover{
    background:#a50000;
    color:white;
}

/* Falling Flowers */

.flower{
    position:fixed;
    top:-10vh;
    animation:fall linear infinite;
    z-index:999;
    opacity:0.7;
}

.flower:nth-child(1){
    left:10%;
    animation-duration:10s;
}

.flower:nth-child(2){
    left:30%;
    animation-duration:12s;
}

.flower:nth-child(3){
    left:50%;
    animation-duration:11s;
}

.flower:nth-child(4){
    left:70%;
    animation-duration:13s;
}

.flower:nth-child(5){
    left:90%;
    animation-duration:10s;
}

@keyframes fall{
    0%{
        transform:translateY(-10vh) rotate(0deg);
    }

    100%{
        transform:translateY(110vh) rotate(360deg);
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

# ---------------- TITLE ---------------- #

st.markdown(
    '<div class="title">💍 शुभ विवाह 💍</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Manish ❤️ Mansi</div>',
    unsafe_allow_html=True
)

# ---------------- AUTO MUSIC ---------------- #

music_html = """
<!DOCTYPE html>
<html>
<body>

<audio id="music" autoplay></audio>

<script>

const songs = [

"https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/jashne_bahara.mp3",

"https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/mangalyam_sathiya.mp3"

];

let currentSong = 0;

const music = document.getElementById("music");

function playSong(index){

    music.src = songs[index];

    music.play();

}

playSong(currentSong);

music.addEventListener("ended", function(){

    currentSong++;

    if(currentSong >= songs.length){
        currentSong = 0;
    }

    playSong(currentSong);

});

</script>

</body>
</html>
"""

components.html(music_html, height=0)

# ---------------- PAGES ---------------- #

pages = [
    "page_1.jpg",
    "page_2.jpg",
    "page_3.jpg"
]

# ---------------- SESSION ---------------- #

if "page" not in st.session_state:
    st.session_state.page = 0

# ---------------- NAVIGATION ---------------- #

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅"):
        if st.session_state.page > 0:
            st.session_state.page -= 1

with col2:
    st.markdown(
        f"""
        <div style='
        text-align:center;
        color:#8B0000;
        font-size:16px;
        font-weight:bold;
        padding-top:5px;
        '>
        Page {st.session_state.page + 1} / {len(pages)}
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    if st.button("➡"):
        if st.session_state.page < len(pages)-1:
            st.session_state.page += 1

# ---------------- IMAGE ---------------- #

st.image(
    pages[st.session_state.page],
    use_container_width=True
)

# ---------------- FOOTER ---------------- #

st.markdown(
    """
    <div style='
    text-align:center;
    color:#8B0000;
    font-size:15px;
    margin-top:5px;
    margin-bottom:0px;
    '>
    ✨ Welcome With Love ✨
    </div>
    """,
    unsafe_allow_html=True
)
