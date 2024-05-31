import streamlit as st
# to run streamlit type in terminal -> streamlit run app.py 
import preprocessor


st.sidebar.title("Whatsapp Chat Analyzer")

# uploading files now
uploaded_file=st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    # file is stream of byte data ,converting it into string 
    data=bytes_data.decode("utf-8")
    # st.text(data)
    # above two lines helps to see txt file on screen

    # calling preprocessor func
    df=preprocessor.preprocess(data)
    st.dataframe(df)