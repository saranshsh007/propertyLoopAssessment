import streamlit as st
from PIL import Image
import io
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from propertyLoopAssessment.src.main import run_router_flow

def save_uploaded_image(uploaded_image):
    img_bytes = uploaded_image.read()
    img = Image.open(io.BytesIO(img_bytes))
    img_path = "uploaded_image.jpg"
    img.save(img_path)
    return img_path

def main():
    st.set_page_config(page_title="Property Assistant", layout="centered")
    st.title("🏠 Smart Property Assistant")

    st.write("This assistant can detect property issues from images or answer tenancy law questions.")

    uploaded_image = st.file_uploader("📷 Upload an image (optional)", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="📸 Uploaded Image", use_container_width=True)

    # User query
    user_text = st.text_input("💬 Enter your question or description:")

    # Location input
    location = st.text_input("📍 Optional: Enter your city or region for tenancy questions:")

    if st.button("Submit"):
        with st.spinner("Thinking..."):
            image_path = save_uploaded_image(uploaded_image) if uploaded_image else ""
            result = run_router_flow(image_path=image_path, user_text=user_text, location=location)
            st.subheader("🧠 Assistant Response")
            st.write(result)

if __name__ == "__main__":
    main()
