import time
import streamlit as st
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image

# Azure credentials
region = "eastus"
key = 'FxjCyxtUo2lJBvkS8h7CcMwMMeGipahnOVgTtyPiJCyjPw5LYu3dJQQJ99ALACYeBjFXJ3w3AAAFACOGzQZV'
endpoint = "https://compt-vision.cognitiveservices.azure.com/"

# Initialize Computer Vision client
credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(endpoint, credentials)

# Streamlit app title
st.title("Interactive OCR Application for Image-to-Text Conversion")

def process_image(file):
    try:
        with open(file, "rb") as read_image:
            rawHttpResponse = client.read_in_stream(read_image, language="en", raw=True)
        operationLocation = rawHttpResponse.headers["Operation-Location"]
        operationId = operationLocation.split("/")[-1]
        
        # Wait for the operation to complete
        while True:
            result = client.get_read_result(operationId)
            if result.status not in ['notStarted', 'running']:
                break
            time.sleep(1)

        # Extract text if operation succeeded
        extracted_text = []
        if result.status == OperationStatusCodes.succeeded:
            for page in result.analyze_result.read_results:
                for line in page.lines:
                    extracted_text.append(line.text)
        return extracted_text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []


# Aadhaar Image upload
st.subheader("Upload Aadhaar Image")
aadhaar_file = st.file_uploader("Choose an Aadhaar image", type=["jpg", "jpeg", "png"])
if aadhaar_file is not None:
    with open("aadhaar_temp.jpg", "wb") as temp_file:
        temp_file.write(aadhaar_file.read())

    st.image(aadhaar_file, caption="Uploaded Aadhaar Image", use_column_width=True)
    st.write("Extracting text from Aadhaar image...")
    aadhaar_text = process_image("aadhaar_temp.jpg")

    if aadhaar_text:
        st.subheader("Extracted Aadhaar Text:")
        st.text("\n".join(aadhaar_text))
    else:
        st.write("No text found in Aadhaar image.")

# General Image upload
st.subheader("Upload Any Other Image")
general_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"], key="general")
if general_file is not None:
    with open("general_temp.jpg", "wb") as temp_file:
        temp_file.write(general_file.read())

    st.image(general_file, caption="Uploaded Image", use_column_width=True)
    st.write("Extracting text from the image...")
    general_text = process_image("general_temp.jpg")

    if general_text:
        st.subheader("Extracted Text:")
        st.text("\n".join(general_text))
    else:
        st.write("No text found in the image.")
