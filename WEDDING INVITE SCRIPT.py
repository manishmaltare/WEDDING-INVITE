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
    font-family:Georgia;
}

/* Main Container */

.block-container{
    padding-top:0rem;
    padding-bottom:0rem;
    max-width:650px;
    padding-left:0rem;
    padding-right:0rem;
}

/* Couple Names */

.subtitle{
    text-align:center;
    color:#b8860b;
    font-size:18px;
    font-weight:bold;
    margin-bottom:8px;
    margin-top:-5px;
}

/* Remove image gaps */

img{
    margin-bottom:8px;
    border-radius:8px;
}

/* Music Button */

.music-btn{
    position:fixed;
    bottom:15px;
    right:15px;
    width:42px;
    height:42px;
    border-radius:50%;
    background:rgba(139,0,0,0.45);
    color:white;
    border:none;
    z-index:9999;
    font-size:18px;
    backdrop-filter: blur(4px);
}

/* Falling Flowers */

.flower{
    position:fixed;
    top:-10vh;
    animation:fall linear infinite;
    z-index:999;
    opacity:0.55;
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

# ---------------- COUPLE NAME ---------------- #

st.markdown(
    '<div class="subtitle">Manish ❤️ Mansi</div>',
    unsafe_allow_html=True
)

# ---------------- MUSIC ---------------- #

music_html = """
<!DOCTYPE html>
<html>

<body>

<button class="music-btn" onclick="startMusic()">♫</button>

<audio id="musicPlayer"></audio>

<script>

const songs = [

"https://raw.githubusercontent.com/manishmaltare/WEDDING-INVITE/main/jashne_bahara.mp3",

"https://raw.githubusercontent.com/manishmaltare/WEDDING-INVITE/main/mangalyam_sathiya.mp3"

];

let currentSong = 0;

const player = document.getElementById("musicPlayer");

function playSong(index){

    player.src = songs[index];

    player.load();

    player.play();

}

function startMusic(){

    playSong(currentSong);

    document.querySelector(".music-btn").style.display = "none";

}

player.addEventListener("ended", function(){

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

# ---------------- ALL PAGES ---------------- #

pages = [
    "page_1.jpg",
    "page_2.jpg",
    "page_3.jpg"
]

for page in pages:

    st.image(
        page,
        use_container_width=True
    )
