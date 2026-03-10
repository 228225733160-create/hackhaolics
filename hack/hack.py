import streamlit as st
import openai

# -----------------------------
# Configure OpenAI API Key
# -----------------------------
openai.api_key = "YOUR_OPENAI_API_KEY"

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="StyleSense - AI Fashion Recommender",
    page_icon="👗",
    layout="centered"
)

st.title("👗 StyleSense")
st.subheader("Generative AI Powered Fashion Recommendation System")

st.write("Get AI-powered outfit suggestions based on your preferences.")

# -----------------------------
# User Inputs
# -----------------------------
gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])

occasion = st.selectbox(
    "Occasion",
    ["Casual", "Party", "College", "Wedding", "Office", "Travel"]
)

season = st.selectbox(
    "Season",
    ["Summer", "Winter", "Rainy", "Spring"]
)

color = st.text_input("Preferred Color")

style = st.selectbox(
    "Fashion Style",
    ["Streetwear", "Minimal", "Formal", "Sporty", "Traditional"]
)

# -----------------------------
# Generate Recommendation
# -----------------------------
if st.button("Generate Outfit Recommendation 👚"):

    prompt = f"""
    Suggest a fashionable outfit for:
    Gender: {gender}
    Occasion: {occasion}
    Season: {season}
    Preferred Color: {color}
    Style: {style}

    Give:
    1. Top wear
    2. Bottom wear
    3. Footwear
    4. Accessories
    5. Styling tips
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content

    st.success("✨ AI Fashion Recommendation")
    st.write(result)

# -----------------------------
# Optional Image Upload
# -----------------------------
st.subheader("Upload Your Outfit (Optional)")

uploaded_file = st.file_uploader("Upload outfit image", type=["jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Your uploaded outfit", use_column_width=True)
    st.info("Image analysis feature can be extended using computer vision models.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("StyleSense | Generative AI Fashion Recommender")