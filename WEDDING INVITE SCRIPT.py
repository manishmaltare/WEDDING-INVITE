import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Wedding Invitation",
    page_icon="💍",
    layout="centered"
)

# ---------------- SESSION ---------------- #

if "page" not in st.session_state:
    st.session_state.page = 0

# ---------------- PAGES ---------------- #

pages = [
    "page_1.jpg",
    "page_2.jpg",
    "page_3.jpg"
]

# ---------------- PAGE FUNCTIONS ---------------- #

def next_page():
    if st.session_state.page < len(pages) - 1:
        st.session_state.page += 1

def prev_page():
    if st.session_state.page > 0:
        st.session_state.page -= 1

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
    margin-top:-5px;
    margin-bottom:2px;
    font-weight:bold;
}

/* Hide Audio Controls */

audio{
    display:none;
}

/* Navigation Buttons */

div.stButton > button:first-child{
    border:none;
    background:rgba(139,0,0,0.35);
    color:white;
    width:42px;
    height:42px;
    border-radius:50%;
    font-size:22px;
    font-weight:bold;
    padding:0px;
    backdrop-filter: blur(4px);
}

div.stButton > button:first-child:hover{
    background:rgba(139,0,0,0.55);
    color:white;
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

# ---------------- COUPLE NAMES ---------------- #

st.markdown(
    '<div class="subtitle">Manish ❤️ Mansi</div>',
    unsafe_allow_html=True
)

# ---------------- BACKGROUND MUSIC ---------------- #

st.markdown("""
<audio id="weddingMusic" autoplay></audio>

<script>

const songs = [

"https://raw.githubusercontent.com/manishmaltare/WEDDING-INVITE/main/jashne_bahara.mp3",

"https://raw.githubusercontent.com/manishmaltare/WEDDING-INVITE/main/mangalyam_sathiya.mp3"

];

let currentSong = 0;

const player = document.getElementById("weddingMusic");

function playSong(index){

    player.src = songs[index];

    player.play();

}

playSong(currentSong);

player.addEventListener("ended", function(){

    currentSong++;

    if(currentSong >= songs.length){
        currentSong = 0;
    }

    playSong(currentSong);

});

</script>
""", unsafe_allow_html=True)

# ---------------- IMAGE ---------------- #

st.image(
    pages[st.session_state.page],
    use_container_width=True
)

# ---------------- NAVIGATION ---------------- #

col1, col2, col3 = st.columns([1,10,1])

with col1:
    st.button(
        "❮",
        on_click=prev_page,
        use_container_width=True
    )

with col3:
    st.button(
        "❯",
        on_click=next_page,
        use_container_width=True
    )
