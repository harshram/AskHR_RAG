# The below frontend code is provided by AWS and Streamlit. I have only modified it to make it look attractive.
import streamlit as st
import rag_backend as demo ### replace rag_backend with your backend filename

st.set_page_config(page_title="HR Q & A with RAG") ### Modify Heading

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">HR Q & A with RAG 🎯</p>' ### Modify Title

st.markdown(new_title,unsafe_allow_html=True) ## Modify Title

if 'vector_index' not in st.session_state :

    with st.spinner("Loading Index"): ###spinner message
        st.session_state.vector_index=demo.hr_index()   ### Your Index Function name from Backend File


input_text = st.text_area("Input Text",label_visibility='collapsed')
go_button = st.button("AskHR",type='primary') ### Button Name

if go_button:
    
  with st.spinner('Loading response.....'):   ### Spinner message
      reponse = demo.hr_rag_response(question=input_text,index=st.session_state.vector_index)   ### replace with RAG Function from backend file
      st.write(reponse)  