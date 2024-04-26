import streamlit as st
import cv2
import pytesseract


def wide_space_default():
    st.set_page_config(layout="wide")


wide_space_default()

img = st.file_uploader("Choose a file", type=["jpg", "png"])


if img is not None:
    filebytes = img.getvalue()
    thresh = st.slider("Threshold", 0, 255, 127)
    maxval = st.slider("Maxval", 0, 255, 255)
    thresh_types = {"THRESH_BINARY": 0, "THRESH_BINARY_INV": 1}
    thresh_type = st.selectbox("Threshold type", thresh_types.keys())

    with open(img.name, 'wb') as f:
        f.write(filebytes)
    image = cv2.imread(img.name)
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, im_bw = cv2.threshold(im_gray, thresh, maxval, thresh_types[thresh_type])

    col1, col2 = st.columns(2)
    with col1:
        st.write("Original")
        st.image(img)
        st.write(pytesseract.image_to_string(image))

    with col2:
        st.write("Processed")
        st.image(im_bw)
        st.write(pytesseract.image_to_string(im_bw))
