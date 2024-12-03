# Azure_OCR

streamlit App- https://interactive-ocr-application-for-image-to-text-conversion.streamlit.app/


## Interactive OCR Application for Image-to-Text Conversion
**Description:**
- Developed a web-based application using **Streamlit** to extract text from images leveraging **Azure Computer Vision OCR API**. The application enables users to upload images, processes them in real-time, and retrieves textual content with high accuracy. The tool is particularly effective for digitizing Aadhaar cards and general documents, showcasing seamless integration with Azure cloud services.

- **Key Features:**
  - **Interactive User Interface:** Created an intuitive and user-friendly interface using Streamlit, allowing users to upload and visualize images before 
    processing.
  - **Text Extraction:** Utilized **Azure Computer Vision OCR API** to extract and analyze text from uploaded images, supporting English and other languages.
  - **Error Handling:** Implemented robust error handling to manage invalid inputs, large files, and API response issues, ensuring a smooth user experience.
  - **Image Preprocessing:** Enhanced OCR accuracy through preprocessing techniques, including resizing and grayscale conversion, using **Pillow.**
- **Tools & Technologies:**
   - **Programming Languages:** Python
   - **Libraries:** Streamlit, Pillow, msrest, Azure SDK (Cognitive Services)
   - **Cloud Services:** Azure Computer Vision
   - **Development Tools:** Visual Studio Code, GitHub
   - **Deployment:** Local development with scope for Azure Web App deployment.
- **Responsibilities:**
   - Designed and implemented the **Streamlit** application for real-time OCR operations.
   - Configured and authenticated the **Azure Computer Vision client** using API keys and endpoint URLs.
   - Developed the `process_image` function to handle file reading, asynchronous API calls, and text extraction.
   - Built and tested the system to process Aadhaar card images and general documents with diverse text patterns.
   - Integrated dynamic feedback and logging mechanisms to enhance user experience and troubleshoot issues.
   - Managed uploaded files securely, incorporating temporary file storage mechanisms.
   - Conducted performance testing and optimization to improve API call efficiency and UI responsiveness.
- **Project Impact:**
   - Demonstrated the potential of integrating **Azure Cognitive Services**  into scalable web applications.
   - Enhanced document digitization workflows, reducing manual effort and improving accuracy.
   - Showcased the ability to bridge **cloud computing** and **data extraction** in real-world applications.


