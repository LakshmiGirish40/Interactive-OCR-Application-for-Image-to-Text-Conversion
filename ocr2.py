import time
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image

# Azure credentials
region = "eastus"
key = 'Enter your Azure API Key'
endpoint = "https://computer-vis-app.cognitiveservices.azure.com/"

# Initialize client
credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(endpoint, credentials)

# Image paths
aadhaar_path = r"C:\Users\laksh\VS_Code\Deep_learning\myenv\Python_Azure\computer_vision_ocr\aadhaar.jpg"
image_path = r"C:\Users\laksh\VS_Code\Deep_learning\myenv\Python_Azure\computer_vision_ocr\image.jpg"

# Function to process image
def process_image(file_path):
    with open(file_path, "rb") as read_image:
        rawHttpResponse = client.read_in_stream(read_image, language="en", raw=True)

    operationLocation = rawHttpResponse.headers["Operation-Location"]
    operationId = operationLocation.split("/")[-1]

    # Wait for operation to complete
    while True:
        result = client.get_read_result(operationId)
        if result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Output results
    if result.status == OperationStatusCodes.succeeded:
        for line in result.analyze_result.read_results[0].lines:
            print(line.text)

# Process both images
print("Processing Aadhaar Image:")
process_image(aadhaar_path)
print("\nProcessing Other Image:")
process_image(image_path)
