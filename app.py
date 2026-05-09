import streamlit as st
from api_calling import note_generator
from PIL import Image

st.title("Viva Questions Generator")
st.markdown("Upload images to generate viva questions")
st.divider()

with st.sidebar:
    st.header("Controls")

    img = st.file_uploader(
        "Upload the photos of your note",
        type=["jpg", "jpeg", "png"]
    )

    pressed = st.button("Click the button to generate", type="primary")

if img is not None:
    st.image(img, caption="Uploaded Image", use_container_width=True)

if pressed:
    if img is None:
        st.error("You must upload an image first.")
    else:
        pil_image = Image.open(img)

        with st.container(border=True):
            st.subheader("Viva Insight")
            generated_note = note_generator(pil_image)
            st.markdown(generated_note)



