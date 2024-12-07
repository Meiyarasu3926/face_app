import os
import base64
import numpy as np
import pandas as pd
import face_recognition
import streamlit as st
from PIL import Image

# Directories
IMAGE_DIR = "employee_photos"
os.makedirs(IMAGE_DIR, exist_ok=True)

TEMP_DIR = "temp_comparison"
os.makedirs(TEMP_DIR, exist_ok=True)

# Helper functions
def encode_image(image_path):
    """Encodes an image to base64 format."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Streamlit interface
st.title("Face Recognition System")

# Image Registration
st.subheader("Register a New Image")
upload_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if upload_image:
    img = Image.open(upload_image)
    st.image(img, caption="Uploaded Image", use_container_width=True)  # Updated to use_container_width

    if st.button("Register Image"):
        file_path = os.path.join(IMAGE_DIR, upload_image.name)
        with open(file_path, "wb") as f:
            f.write(upload_image.getbuffer())
        
        try:
            image = face_recognition.load_image_file(file_path)
            face_encoding = face_recognition.face_encodings(image)[0]
            # Save face encoding to a file (optional step, for storage)
            np.save(file_path + ".npy", face_encoding)
            st.success(f"Image registered successfully: {upload_image.name}")
        except IndexError:
            st.error("No face detected in the uploaded image.")
        
# Image Comparison
st.subheader("Compare an Image")

upload_image_to_compare = st.file_uploader("Upload Image to Compare", type=["jpg", "jpeg", "png"])

if upload_image_to_compare:
    img_to_compare = Image.open(upload_image_to_compare)
    st.image(img_to_compare, caption="Image to Compare", use_container_width=True)  # Updated to use_container_width

    if st.button("Compare Image"):
        temp_file_path = os.path.join(TEMP_DIR, upload_image_to_compare.name)
        with open(temp_file_path, "wb") as f:
            f.write(upload_image_to_compare.getbuffer())
        
        try:
            uploaded_image = face_recognition.load_image_file(temp_file_path)
            uploaded_encoding = face_recognition.face_encodings(uploaded_image)[0]
        except IndexError:
            st.error("No face detected in the uploaded image.")
            os.remove(temp_file_path)  

        match_result = None
        for existing_file in os.listdir(IMAGE_DIR):
            existing_file_path = os.path.join(IMAGE_DIR, existing_file)
            try:
                existing_encoding = np.load(existing_file_path + ".npy")
                match = face_recognition.compare_faces([existing_encoding], uploaded_encoding)
                distance = face_recognition.face_distance([existing_encoding], uploaded_encoding)[0]
                similarity = (1 - distance) * 100

                if match[0]:
                    match_result = {"match": True, "filename": existing_file, "similarity": similarity}
                    break
            except (IndexError, FileNotFoundError, ValueError):
                continue
        
        if match_result:
            st.success(f"Match found with {match_result['filename']}! Similarity: {match_result['similarity']:.2f}%")
        else:
            st.error("No matching image found.")
        
        os.remove(temp_file_path)  # Cleanup temporary image
