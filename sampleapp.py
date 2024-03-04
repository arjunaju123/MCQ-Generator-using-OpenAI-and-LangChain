import streamlit as st
import pandas as pd

def read_text_file(file):
    # Read text file
    text = file.read()
    return text

def read_pdf_file(file):
    # Read PDF file
    pdf = pdftotext.PDF(file)
    text = "\n\n".join(pdf)
    return text

def main():
    st.title("File Upload Example")
    st.write("Upload a text file or a PDF file.")

    file = st.file_uploader("Upload file", type=["txt", "pdf"])

    if file is not None:
        file_type = file.type
        if file_type == "text/plain":
            text = read_text_file(file)
            st.write("Text content:")
            st.write(text)
        elif file_type == "application/pdf":
            text = read_pdf_file(file)
            st.write("PDF content:")
            st.write(text)
        else:
            st.error("Unsupported file type. Please upload a text file or a PDF file.")

if __name__ == "__main__":
    main()
