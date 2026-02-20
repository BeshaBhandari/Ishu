import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ishke's Surprise Universe ✨",
    page_icon="💖",
    layout="wide"
)

# --- CUSTOM CSS FOR GEN Z AESTHETIC ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    /* Main Background & Font */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif;
        color: #d63384;
        text-align: center;
        text-transform: capitalize;
        letter-spacing: 1px;
    }
    
    /* Hide default Streamlit elements for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* --- CARDS & CONTAINERS --- */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        text-align: center;
        transition: all 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(214, 51, 132, 0.25);
    }

    /* Image Styling */
    .polaroid {
        border: 10px solid #fff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-radius: 5px;
        transition: transform 0.3s;
    }
    .polaroid:hover {
        transform rotate(1deg) scale(1.02);
    }

    /* Custom Buttons */
    .stButton > button {
        background-image: linear-gradient(45deg, #ff6b6b, #ff8e53);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 10px 25px;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.6);
    }
    
    /* Nav Buttons Specifics */
    .nav-btn {
        background-image: linear-gradient(to right, #8fd3f4, #84fab0) !important;
        color: #444 !important;
        width: 100%;
    }

    /* Quotes */
    .quote-box {
        background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
        padding: 25px;
        border-radius: 20px;
        font-style: italic;
        color: #333;
        margin: 20px 0;
        text-align: center;
        border: 2px solid white;
    }

    /* Video Section */
    .video-wrapper {
        border-radius: 20px;
        overflow: hidden;
        border: 8px solid white;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        margin-top: 20px;
    }

    /* Footer */
    .footer-sticker {
        background: linear-gradient(45deg, #ff9a9e, #fad0c4);
        padding: 40px;
        border-radius: 30px 30px 0 0;
        text-align: center;
        color: white;
        box-shadow: 0 -10px 30px rgba(214, 51, 132, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("✨ A Surprise for Ishke Piske 💖")
st.markdown("<div style='text-align: center; color: #666; font-size: 1.2rem;'>Tap the boxes to reveal the magic! 🌟</div>", unsafe_allow_html=True)
st.markdown("---")

# --- SECTION 1: SURPRISE IMAGE BOXES ---
st.header("Beautiful Memories 🌟")

beautiful_images = {
    "Eyes 👁️": {"path": "eyes.jpg", "desc": "Your soul is sparkling! ✨"},
    "White Dress 👗": {"path": "white dress.jpg", "desc": "Elegant queen vibes 👑"},
    "Twitter DP 🐦": {"path": "twitter_dp.jpg", "desc": "Classic Ishkka aesthetic 😍"},
    "Grok Tweet 💖": {"path": "grok_tweet.jpg", "desc": "Bestie moments 💖😭"},
}

# Initialize Session State
if 'revealed' not in st.session_state:
    st.session_state.revealed = {key: False for key in beautiful_images.keys()}

# Grid Layout
cols = st.columns(4)

for idx, (title, details) in enumerate(beautiful_images.items()):
    with cols[idx]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        if not st.session_state.revealed[title]:
            st.markdown(f"### 🎁 {title}")
            if st.button(f"Open 🔓", key=f"btn_{title}"):
                st.session_state.revealed[title] = True
                st.rerun()
        else:
            try:
                img = Image.open(details["path"])
                # Adding a little rotation for polaroid effect
                st.image(img, use_container_width=True, output_format="PNG")
                st.markdown(f"**{details['desc']}**")
                if st.button("Close ❤️", key=f"btn_close_{title}"):
                    st.session_state.revealed[title] = False
                    st.rerun()
            except FileNotFoundError:
                st.error("Image not found 😢")
        
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --- SECTION 2: FAMILY SLIDESHOW ---
st.header("Family Vibes 👨‍👩‍👧‍👦")

family_images = {
    "With Sister 👧": {"path": "her_sister.jpg", "quote": "Sisters are different flowers from the same garden. 🌸"},
    "Group with Sisters 👩‍👧‍👧": {"path": "her_family.jpg", "quote": "Family is everything. 💖"},
    "With Mom 👩": {"path": "her_mom.jpg", "quote": "A mother's love is the fuel that enables a normal human being to do the impossible. 🌟"},
}

family_titles = list(family_images.keys())
family_paths = [d["path"] for d in family_images.values()]
family_quotes = [d["quote"] for d in family_images.values()]

if 'fam_index' not in st.session_state:
    st.session_state.fam_index = 0

# Main Column for Image
col_center = st.columns([1])[0]

with col_center:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    try:
        st.image(family_paths[st.session_state.fam_index], caption=family_titles[st.session_state.fam_index], use_container_width=True, output_format="PNG")
        st.markdown(f"<div class='quote-box'>{family_quotes[st.session_state.fam_index]}</div>", unsafe_allow_html=True)
    except:
        st.error("Image not found")
    st.markdown('</div>', unsafe_allow_html=True)

# Navigation Row (Centered with gap)
col_prev, col_gap, col_next = st.columns([2, 1, 2])

with col_prev:
    if st.button("⬅️ Prev", key="prev_fam"):
        st.session_state.fam_index = (st.session_state.fam_index - 1) % len(family_titles)
        st.rerun()

with col_next:
    if st.button("Next ➡️", key="next_fam"):
        st.session_state.fam_index = (st.session_state.fam_index + 1) % len(family_titles)
        st.rerun()

st.markdown("---")

# --- SECTION 3: QUOTES ---
st.header("Heart Notes 💬")

quotes = [
    "You are the light in my darkest days. 🌟",
    "True friends are never apart, maybe in distance but never in heart. ❤️",
    "A friend is someone who knows all about you and still loves you. 💕",
    "The greatest gift of life is friendship, and I have received it. 🎁",
    "Good friends are like stars. You don't always see them, but you know they're always there. ⭐",
]

if 'quote_idx' not in st.session_state:
    st.session_state.quote_idx = 0

# Styled Quote Container
st.markdown(f"""
<div class="quote-box" style="font-size: 20px; font-family: 'Poppins', sans-serif;">
    "{quotes[st.session_state.quote_idx]}"
</div>
""", unsafe_allow_html=True)

col_q_prev, col_q_next = st.columns([1,1])
with col_q_next:
    if st.button("Next Quote 💡"):
        st.session_state.quote_idx = (st.session_state.quote_idx + 1) % len(quotes)
        st.rerun()

st.markdown("---")

# --- SECTION 4: VIDEOS ---
st.header("A Special Message To You 🎥")

video_files = ["video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4"]
video_names = ["Vibe 1 🎵", "Vibe 2 🎶", "Vibe 3 🎞️", "Vibe 4 🎆"]

# Use a select slider or radio for Gen Z look
choice = st.select_slider(
    "Pick a video:",
    options=video_names,
    value=video_names[0],
    label_visibility="collapsed"
)
video_idx = video_names.index(choice)

if video_idx < len(video_files):
    st.markdown('<div class="video-wrapper">', unsafe_allow_html=True)
    st.video(video_files[video_idx])
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <h3>You are amazing, Ishkka! Keep shining! 🌈</h3>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div class="footer-sticker">
    <h2>Thank You for Being You! 💖</h2>
    <p style='font-size: 18px;'>
        Dear Ishkka,<br>
        Your presence is a gift. You bring joy, laughter, and warmth. 
        <br><b>Remember, you are loved beyond measure!</b> 🌈
    </p>
    <div style='font-size: 60px; margin-top: 20px;'>💖🤍💖</div>
    <p style="font-size: 12px; margin-top: 20px; opacity: 0.8;">Made with ❤️ just for you</p>
</div>
""", unsafe_allow_html=True)
