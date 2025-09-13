import cv2 as cv
import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Sketchify", layout="wide")

st.title("Sketchify")
st.write("Upload an image and choose a transformation below:")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv.imdecode(file_bytes, 1)
    img = cv.resize(img, (500, 300))

    # User chooses effect on screen
    choice = st.radio(
        "Select an Effect:",
        ["Original", "Pencil Sketch", "Cartoon", "Grayscale", "Edge Detection", "Blur"],
        horizontal=True
    )

    output = None  # processed image

    if choice == "Original":
        output = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    elif choice == "Grayscale":
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        output = gray

    elif choice == "Pencil Sketch":
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        inverted = cv.bitwise_not(gray)
        blur = cv.GaussianBlur(inverted, (21, 21), 0)
        inverted_blur = cv.bitwise_not(blur)
        sketch = cv.divide(gray, inverted_blur, scale=256.0)
        output = sketch

    elif choice == "Cartoon":
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur = cv.medianBlur(gray, 5)
        edges = cv.adaptiveThreshold(
            blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9
        )
        color = cv.bilateralFilter(img, 9, 300, 300)
        cartoon = cv.bitwise_and(color, color, mask=edges)
        output = cv.cvtColor(cartoon, cv.COLOR_BGR2RGB)

    elif choice == "Edge Detection":
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, 100, 200)
        output = edges

    elif choice == "Blur":
        blur = cv.GaussianBlur(img, (21, 21), 0)
        output = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

    # Show result
    col1, col2 = st.columns(2)
    with col1:
        st.image(cv.cvtColor(img, cv.COLOR_BGR2RGB), caption="Original",)
    with col2:
        st.image(
            output,
            caption=choice,
            channels="GRAY" if choice in ["Pencil Sketch", "Grayscale", "Edge Detection"] else "RGB"
        )

    # Download button
    result = Image.fromarray(output)
    st.download_button(
        label=f"Download {choice} Image",
        data=result.tobytes(),
        file_name=f"{choice.lower().replace(' ', '_')}_output.jpg",
        mime="image/jpeg"
    )
