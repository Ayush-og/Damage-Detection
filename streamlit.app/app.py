import streamlit as st
import requests

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded File", use_container_width=True)

    # Send file to FastAPI
    response = requests.post(
        "http://127.0.0.1:9001/predict",
        files={"file": uploaded_file}
    )

    if response.status_code == 200:
        result = response.json()
        st.info(f"Predicted Class: {result['prediction']}")
    else:
        st.error("Error getting prediction from API")