import streamlit as st
from pypdf import PdfMerger
from tempfile import NamedTemporaryFile

st.set_page_config(page_title="PDF Merger", layout="centered")

st.title("PDF Merger Tool")
st.write("Upload multiple pdf files and merge them into one.")

upload_pdf = st.file_uploader("Choose first pdf", "pdf", accept_multiple_files=True)

def main():
    if upload_pdf is not None:
        if st.button("Merge PDFs"):
            merger = PdfMerger()

            for pdf_file in upload_pdf:
                merger.append(pdf_file)
            
            with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                merger.write(tmp_file.name)
                merger.close()

                with open(tmp_file.name, "rb") as f:
                    st.download_button(
                        label="Download Merged pdf",
                        data=f,
                        file_name="merged_output.pdf",
                        mime="application/pdf"
                    )
            
            st.success("PDFs merged successfully!")

if __name__=="__main__":
    main()