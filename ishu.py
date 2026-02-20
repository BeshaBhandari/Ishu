import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="A App for you, Ishkka 💖", page_icon="💖")


# Add a subtitle
st.subheader("Thank you for being there for me! 🫶")

# Display images with titles and descriptions
st.header("Beautiful Moments 🌟")
beautiful_images = {
    "Eyes 👁️": {
        "path": "eyes.jpg",
        "description": "A glimpse into your beautiful soul through your eyes. ✨"
    },
    "In White Dress 👗": {
        "path": "white dress.jpg",
        "description": "You look stunning in this elegant white dress. 😍"
    },
    "Old Twitter DP 🖼️": {
        "path": "twitter_dp.jpg",
        "description": "A cherished memory captured in your old Twitter profile picture. 💭"
    },
}

# Display each image with its title and description
for title, details in beautiful_images.items():
    img = Image.open(details["path"])
    st.image(img, caption=title, use_container_width=True)
    st.write(details["description"])

# Quotes list with emojis
quotes = [
    "You are the light in my darkest days. 🌟",
    "True friends are never apart, maybe in distance but never in heart. ❤️",
    "Friendship is born at that moment when one person says to another, 'What! You too? I thought I was the only one.' 🤝",
    "A friend is someone who knows all about you and still loves you. 💕",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. 🤫",
    "The greatest gift of life is friendship, and I have received it. 🎁",
    "A true friend is the greatest of all blessings. 🙌",
    "Friendship is the only cement that will ever hold the world together. 🌍",
    "Good friends are like stars. You don't always see them, but you know they're always there. ⭐",
    "A friend is one who overlooks your broken fence and admires the flowers in your garden. 🌸"
]

# Display family images with long quotes
st.header("Family Moments 👨‍👩‍👧‍👦")
family_images = {
    "With Sister 👧": {
        "path": "her_sister.jpg",
        "quote": "Sisters are different flowers from the same garden. 🌸 They share a bond that is unbreakable, filled with laughter, secrets, and memories that last a lifetime. No matter where life takes us, I know we will always have each other's backs."
    },
    "Group with Sisters and Mom 👩‍👧‍👧": {
        "path": "her_family.jpg",
        "quote": "Family is not an important thing, it's everything. 💖 This moment captures the love and joy we share as a family, reminding me that no matter the distance, our hearts are always connected."
    },
    "With Mom 👩": {
        "path": "her_mom.jpg",
        "quote": "A mother's love is the fuel that enables a normal human being to do the impossible. 🌟 This picture represents the unconditional love and support that my mom has always given me, guiding me through life's challenges."
    },
}

# Create a slideshow for Family Moments
family_image_titles = list(family_images.keys())
family_image_paths = [details["path"] for details in family_images.values()]
family_image_quotes = [details["quote"] for details in family_images.values()]

# Automatic slideshow for Family Moments
if 'family_index' not in st.session_state:
    st.session_state.family_index = 0

# Display family images in a loop
st.image(family_image_paths[st.session_state.family_index], caption=family_image_titles[st.session_state.family_index], use_container_width=True)
st.write(family_image_quotes[st.session_state.family_index])

if st.button("Next Family Moment"):
    st.session_state.family_index = (st.session_state.family_index + 1) % len(family_image_titles)

# Automatic quote display
st.header("Quotes 💬")
quote_placeholder = st.empty()
quote_index = st.session_state.get('quote_index', 0)

# Display quotes in a loop
if st.button("Next Quote"):
    quote_placeholder.markdown(f"<div style='background-color: #f0f2f5; padding: 10px; border-radius: 5px; font-size: 24px;'>{quotes[quote_index]}</div>", unsafe_allow_html=True)
    quote_index = (quote_index + 1) % len(quotes)
    st.session_state.quote_index = quote_index

# Video section
st.header("Videos")
video_files = [ "video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4"]  # Add your video file paths here
video_index = st.session_state.get('video_index', 0)

if video_index < len(video_files):
    st.video(video_files[video_index])

    if st.button("Next Video , You are amazing, Ishkka! Keep shining! 🌟"):
        video_index = (video_index + 1) % len(video_files)
        st.session_state.video_index = video_index
        st.markdown("<div style='color: #ff6347; font-size: 20px;'>You are amazing, Ishkka! Keep shining! 🌈</div>", unsafe_allow_html=True)

# Add some CSS for better styling
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f5;
    }
    h1, h2, h3 {
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

st.header("Some Memories from twitter 💖😭")
st.image("grok_tweet.jpg", caption="A snapshot of our beautiful friendship! 💖")

st.markdown("""

<div style='font-size: 18px; color: #4B0082;'> Dear Ishu,<br> Every moment spent with you is a treasure. Your laughter lights up my days, and your kindness inspires me to be better. Our friendship is a beautiful journey filled with shared dreams, endless support, and unforgettable memories. Thank you for being you! Here's to many more adventures together! 🌟<br> With all my love,<br> [Truthiee] </div> """, unsafe_allow_html=True)


# Footer Note
st.markdown("""
<div style='text-align: center; padding: 20px; background-color: #f0f2f5; border-top: 2px solid #4B0082;'>
    <h3 style='color: #4B0082;'>Thank You for Being You! 💖</h3>
    <p style='font-size: 18px; color: #333;'>
        Dear Ishkka,<br>
        Your presence in my life is a gift I cherish every day. You bring joy, laughter, and warmth to my world. 
        Thank you for being my confidant, my cheerleader, and my friend. 
        May our bond continue to grow stronger with each passing day. 
        Remember, you are loved beyond measure! 🌈
    </p>
</div>
""", unsafe_allow_html=True)
