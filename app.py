from PyPDF2 import PdfReader
import streamlit as st
from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    :param pdf_file: Uploaded PDF file
    :return: Extracted text
    """
    text = ""
    try:
        # Read the PDF file from the uploaded file
        reader = PdfReader(pdf_file)

        # Iterate through each page and extract text
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        st.error(f"Error occurred: {e}")
    return text

def write_text_to_file(text):
    """
    Writes text to a buffer.

    :param text: Text to write
    :return: StringIO buffer
    """
    buffer = io.BytesIO()
    buffer.write(text.encode('utf-8'))
    buffer.seek(0)
    return buffer

def main():
    st.title("PDF to Text Converter")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file is not None:
        extracted_text = extract_text_from_pdf(uploaded_file)

        # Replace 'output.txt' with the desired output file name
        output_file_name = st.text_input("Enter the output file name", 'output.txt')

        if st.button("Extract Text"):
            if extracted_text.strip():
                buffer = write_text_to_file(extracted_text)
                st.download_button(
                    label="Download Text File",
                    data=buffer,
                    file_name=output_file_name,
                    mime='text/plain'
                )
            else:
                st.warning("No text extracted from the PDF.")

if __name__ == '__main__':
    main()