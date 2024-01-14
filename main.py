# Importing the necessary libraries
import streamlit as st
import gemini_pdf as gp



def main():
    # Setting the page configuration for the Streamlit app
    st.set_page_config("Chat PDF")
    # Displaying a header for the app
    st.header("Chat with MultiplePDFs")

    # Getting user input for the question
    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        # Processing the user input
        gp.user_input(user_question)

    with st.sidebar:
        # Displaying a sidebar menu
        st.title("Menu:")
        # Allowing the user to upload multiple PDF files
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                # Extracting text from the uploaded PDF files
                raw_text = gp.get_pdf_text(pdf_docs)
                # Splitting the text into chunks
                text_chunks = gp.get_text_chunks(raw_text)
                # Creating a vector store for the text chunks
                gp.get_vector_store(text_chunks)
                # Displaying a success message
                st.success("Done! now you are ready to ask questions")

if __name__ == "__main__":
    # Running the main function
    main()