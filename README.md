## PDF to Text Converter

This Streamlit application provides a simple and intuitive interface for extracting text from PDF files. Users can upload a PDF and download the extracted text as a .txt file.

## Link for the Application: 
https://pdftotxt.streamlit.app/

## Usage

- Click the "Upload a PDF file" button to select and upload a PDF file.
- Enter the desired name for the output text file in the input box.
- Click "Extract Text" to process the uploaded file.
- Click the "Download Text File" button to save the extracted text to your system.


## Features
- Upload PDF: Users can upload a PDF file from their local system.
  
- Extract Text: The application reads and extracts text from each page of the uploaded PDF.

- Download Extracted Text: Users can download the extracted text as a text file. The file name can be customized.

## Installation

To run this application locally, you need Python installed on your system. If you don't have Python installed, download and install it from python.org. This application also requires Streamlit, PyPDF2, and a few other libraries.


    pip install -r requirements.txt

## Running the Application 

    streamlit run app.py


The application will open in your default web browser.


Note

    The application extracts text based on the PDF's internal structure. Some PDFs, especially those with complex layouts or scanned images, may not extract text accurately.
    The application currently does not support batch processing. Files must be processed one at a time.
