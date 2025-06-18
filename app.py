import streamlit as st
from transformers import pipeline
import os

# Load the model
generator = pipeline('text-generation', model='gpt2')

st.title("AI Product Copy Generator")

# Sidebar for additional options
st.sidebar.header("Options")
tone = st.sidebar.selectbox("Select tone:", ["Creative", "Formal", "Casual"])
num_variations = st.sidebar.slider("Number of variations", 1, 2, 1)
max_length = st.sidebar.slider("Maximum length of generated text", 50, 200, 150)

# Input
bullets = st.text_area("Enter bullet points or keywords:", height=100)

if st.button("Generate"):
    if not bullets.strip():
        st.warning("Please enter some bullet points or keywords.")
    else:
        prompt = f"Write {num_variations} variations of product marketing copy based on these points:\n{bullets}\nTone: {tone}."
        response = generator(prompt, max_length=max_length * num_variations, num_return_sequences=num_variations, temperature=0.8 if tone == "Creative" else 0.5 if tone == "Casual" else 0.3)
        for i, choice in enumerate(response):
            # Highlight keywords
            text = choice['generated_text'].strip()
            for word in bullets.split():
                if len(word) > 2:
                    text = text.replace(word, f"**:orange[{word}]**")
            st.markdown(f"**Variation {i+1}:**\n{text}", unsafe_allow_html=True)

# Display a footer
st.markdown("---")
st.markdown("Built with Streamlit and Hugging Face Transformers") 