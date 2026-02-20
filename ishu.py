import streamlit as st
from PIL import Image
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="A Surprise for Ishkka 💖", 
    page_icon="🎁", 
    layout="wide"
)

# --- CUSTOM CSS FOR EYE-CATCHING UI ---
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }
    
    /* Custom Fonts and Headers */
    h1, h2, h3 {
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
        color: #d63384;
        text-align: center;
    }
    
    /* The "Gift Box" Container */
    .gift-card {
        background-color: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 10px 25px rgba(214, 51, 132, 0.2);
        text-align: center;
        transition: transform 0.3s;
        border: 2px solid #ffdee9;
    }
    .gift-card:hover {
        transform: scale(1.02);
    }

    /* The Revealed Image Animation */
    .revealed-img {
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        animation: popIn 0.5s ease-out;
    }

    @keyframes popIn {
        0% { opacity: 0; transform: scale(0.5); }
        80% { transform: scale(1.05); }
        100% { opacity: 1; transform: scale(1); }
    }

    /* Custom Buttons */
    .stButton > button {
        background-image: linear-gradient(to right, #ff512f, #dd2476);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 10px 24px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(221, 36, 118, 0.4);
    }

    /* Quote Styling */
    .quote-box {
        background: linear-gradient(45deg, #ffe6fa, #e6f2ff);
        padding: 20px;
        border-left: 5px solid #d63384;
        border-radius: 10px;
        font-style: italic;
        color: #444;
        margin-bottom: 20px;
    }

    /* Video Container */
    .video-container {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        border: 5px solid white;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🎁 A Special App for You, Ishkka! 💖")
st.markdown("<div style='text-align: center; color: #888;'>Tap the boxes to reveal the surprises!</div>", unsafe_allow_html=True)
st.markdown("---")

# --- SECTION 1: SURPRISE IMAGE BOXES ---
st.header("Beautiful Moments 🌟")

# Dictionary of images
beautiful_images = {
    "Eyes 👁️": {"path": "eyes.jpg", "desc": "A glimpse into your beautiful soul. ✨"},
    "White Dress 👗": {"path": "white dress.jpg", "desc": "You look stunning in this elegant white dress. 😍"},
    "Old Twitter DP 🖼️": {"path": "twitter_dp.jpg", "desc": "A cherished memory captured in time. 💭"},
    "Grok Tweet 💖": {"path": "grok_tweet.jpg", "desc": "A snapshot of our beautiful friendship! 💖😭"},
}

# Create a grid (3 columns)
cols = st.columns(len(beautiful_images))

# Initialize session state for toggling images if not exists
if 'revealed' not in st.session_state:
    st.session_state.revealed = {key: False for key in beautiful_images.keys()}

# Generate Cards
for idx, (title, details) in enumerate(beautiful_images.items()):
    with cols[idx]:
        st.markdown(f"<div class='gift-card'>", unsafe_allow_html=True)
        
        if not st.session_state.revealed[title]:
            st.markdown(f"### 🎁 {title}")
            st.markdown("Click to open!")
            if st.button(f"Open Gift 🎀", key=f"btn_{title}"):
                st.session_state.revealed[title] = True
                st.rerun()
        else:
            try:
                img = Image.open(details["path"])
                st.image(img, caption=title, use_container_width=True, output_format="PNG")
                st.markdown(f"<p style='color:#d63384; font-weight:bold;'>{details['desc']}</p>", unsafe_allow_html=True)
                if st.button("Close 💔", key=f"btn_close_{title}"):
                    st.session_state.revealed[title] = False
                    st.rerun()
            except FileNotFoundError:
                st.error("Image not found")
        
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --- SECTION 2: FAMILY SLIDESHOW ---
st.header("Family Moments 👨‍👩‍👧‍👦")

family_images = {
    "With Sister 👧": {"path": "her_sister.jpg", "quote": "Sisters are different flowers from the same garden. 🌸"},
    "Group with Sisters 👩‍👧‍👧": {"path": "her_family.jpg", "quote": "Family is not an important thing, it's everything. 💖"},
    "With Mom 👩": {"path": "her_mom.jpg", "quote": "A mother's love is the fuel that enables a normal human being to do the impossible. 🌟"},
}

# Carousel Logic
family_titles = list(family_images.keys())
family_paths = [d["path"] for d in family_images.values()]
family_quotes = [d["quote"] for d in family_images.values()]

if 'fam_index' not in st.session_state:
    st.session_state.fam_index = 0

col_left, col_mid, col_right = st.columns([1, 4, 1])

with col_mid:
    st.markdown('<div class="gift-card">', unsafe_allow_html=True)
    try:
        st.image(family_paths[st.session_state.fam_index], caption=family_titles[st.session_state.fam_index], use_container_width=True, output_format="PNG")
        st.markdown(f"<div class='quote-box'>{family_quotes[st.session_state.fam_index]}</div>", unsafe_allow_html=True)
    except:
        st.error("Image not found")
    st.markdown('</div>', unsafe_allow_html=True)

# Navigation Buttons
with col_left:
    if st.button("⬅️ Prev"):
        st.session_state.fam_index = (st.session_state.fam_index - 1) % len(family_titles)
        st.rerun()

with col_right:
    if st.button("Next ➡️"):
        st.session_state.fam_index = (st.session_state.fam_index + 1) % len(family_titles)
        st.rerun()

st.markdown("---")

# --- SECTION 3: QUOTES ---
st.header("Words from Heart 💬")

quotes = [
    "You are the light in my darkest days. 🌟",
    "True friends are never apart, maybe in distance but never in heart. ❤️",
    "A friend is someone who knows all about you and still loves you. 💕",
    "The greatest gift of life is friendship, and I have received it. 🎁",
    "Good friends are like stars. You don't always see them, but you know they're always there. ⭐",
]

if 'quote_idx' not in st.session_state:
    st.session_state.quote_idx = 0

# Display Quote in a styled box
st.markdown(f"""
<div class="quote-box" style="font-size: 20px; text-align: center;">
    "{quotes[st.session_state.quote_idx]}"
</div>
""", unsafe_allow_html=True)

if st.button("Next Inspiration 💡"):
    st.session_state.quote_idx = (st.session_state.quote_idx + 1) % len(quotes)
    st.rerun()

st.markdown("---")

# --- SECTION 4: VIDEOS ---
st.header("Fun Videos 🎥")

video_files = ["video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4"]
video_names = ["Video 1 🎵", "Video 2 🎶", "Video 3 🎞️", "Video 4 🎆"]

# Use a select box to choose video (Cooler UI)
choice = st.selectbox("Choose a video to watch:", video_names, label_visibility="collapsed")
video_idx = video_names.index(choice)

if video_idx < len(video_files):
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    st.video(video_files[video_idx])
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; margin-top: 10px;">
        <h3>You are amazing, Ishkka! Keep shining! 🌈</h3>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 30px; background-color: #fff0f5; border-radius: 20px;'>
    <h2 style='color: #d63384;'>Thank You for Being You! 💖</h2>
    <p style='font-size: 18px; color: #555;'>
        Dear Ishkka,<br>
        Your presence in my life is a gift I cherish every day. You bring joy, laughter, and warmth to my world. 
        Thank you for being my confidant and my friend. 
        <br><b>Remember, you are loved beyond measure!</b> 🌈
    </p>
    <div style='font-size: 50px;'>💖🤍💖</div>
</div>
""", unsafe_allow_html=True)
