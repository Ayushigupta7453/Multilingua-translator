import streamlit as st
from translator import translate_text

st.set_page_config(page_title="AI Translator", layout="wide")

# Custom CSS for navbar
st.markdown("""
    <style>
        .navbar {
            background-color: #4A90E2;
            padding: 1rem;
            color: white;
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar">🌐 AI-Powered Multilingual Translator</div>', unsafe_allow_html=True)

# Create two columns
left_col, right_col = st.columns([1, 2])

# Left Column: Image
with left_col:
    st.image("https://www.dtstranslates.com/wp-content/uploads/2020/09/interpreter-vs-translator-1.jpeg", use_column_width=True)

# Right Column: Text input and output
with right_col:
    st.subheader("Enter Text to Translate")
    text_to_translate = st.text_area("", height=100)

    languages = [
        "Hindi", "Spanish", "French", "German", "Japanese", "Chinese", "Arabic",
        "Russian", "Korean", "Portuguese", "Italian", "Bengali", "Urdu", "Tamil"
    ]
    target_language = st.selectbox("Select Target Language", languages)

    if st.button("Translate"):
        if text_to_translate.strip() == "":
            st.warning("Please enter text to translate.")
        else:
            with st.spinner("Translating..."):
                translation = translate_text(text_to_translate, target_language)
                st.success("Translation Complete!")
                st.markdown("### 📝 Translated Text:")
                st.text_area("Result", value=translation, height=150)
