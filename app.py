import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Jackson Hamisi Wambali | Portfolio", layout="centered")

# Header
st.title("Jackson Hamisi Wambali")
st.subheader("AI and Systems Developer | Conservation Tech Enthusiast")

# Bio
st.markdown("""
Hello! I'm Jackson, a passionate developer focused on real-world tech innovations — from smart airport systems to AI-driven bird species recognition.
Explore my work, view my CV, and check out my GitHub projects.
""")

# Download CV
with open("CV/Jackson_CV.pdf", "rb") as f:
    st.download_button("📄 Download My CV", f, file_name="Jackson_CV.pdf")

# Featured Project
st.markdown("## 📌 Featured Project: Bird Species Identifier (Tanzania)")
col1, col2 = st.columns([1, 1])
with col1:
    st.image("images/Screenshot_2025-05-23_09.39.52.png", caption="Prediction Output", use_container_width=True)
with col2:
    st.image("images/Screenshot_2025-05-23_09.40.11.png", caption="Detailed Bird Information", use_container_width=True)

st.markdown("""
This tool uses image recognition and mapping to identify bird species and display their habitat, conservation status, and migration data — empowering Tanzanian conservation efforts.
""")
