import streamlit as st
import streamlit.components.v1 as components

def show_welcome_page():

    st.markdown(
        """
    <style>
    span[data-baseweb="tag"] {
    background-color: blue !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    HtmlFile = open("index.html", 'r', encoding='utf-8')

    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, width=900 , height=650, scrolling=False)