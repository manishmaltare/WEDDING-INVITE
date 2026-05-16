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
    width:45px;
    height:45px;
    border-radius:50%;
    background:rgba(139,0,0,0.45);
    color:white;
    border:none;
    z-index:9999;
    font-size:20px;
    backdrop-filter: blur(4px);
    cursor:pointer;
}

/* Venue Location Button */

.location-btn{
    position:fixed;
    bottom:75px;
    right:15px;
    padding:12px 20px;
    border-radius:35px;
    background:rgba(139,0,0,0.60);
    color:white;
    display:flex;
    align-items:center;
    justify-content:center;
    gap:10px;
    text-decoration:none;
    z-index:9999;
    font-size:26px;
    font-weight:bold;
    backdrop-filter: blur(4px);
    box-shadow:0 4px 10px rgba(0,0,0,0.2);
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
    '<div class="subtitle">Manish ❤️ Mansi (Divya)</div>',
    unsafe_allow_html=True
)

# ---------------- MUSIC + LOCATION ---------------- #

music_html = """
<!DOCTYPE html>
<html>

<body>

<!-- Music Button -->
<button class="music-btn" onclick="startMusic()">♫</button>

<!-- Venue Location Button -->
<a 
    class="location-btn"
    href="https://maps.google.com/?q=22.737284863576736,75.77342718392956"
    target="_blank"
    title="Venue Location"
>
📍 Venue Location
</a>

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

components.html(music_html, height=140)

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
