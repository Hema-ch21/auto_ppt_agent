import streamlit as st
from agent import run

st.title("🚀 AI PPT Generator")

topic = st.text_input("Enter Topic")

if st.button("Generate PPT"):
    if topic:
        with st.spinner("Generating PPT..."):
            file_path = run(topic)

        st.success("PPT Generated Successfully!")

        st.download_button(
            "Download PPT",
            open(file_path, "rb"),
            file_name="generated.pptx"
        )