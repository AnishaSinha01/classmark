import streamlit as st

def style_background_home():
    st.markdown(
        """
        <style>

        .stApp {
        background: #6FA893 !important;
        }

        .stApp div[data-testid="stColumn"]{
            background-color:#EAF3F0 !important;
            padding:1.8rem !important;
            border-radius: 2rem !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

def style_background_dashboard():
    st.markdown(
        """
        <style>

        .stApp {
        background: #EAF3F0 !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

         /* Hide Top Bar of streamlit */
             
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }
        
        h1 {
            font-family: 'Fraunces', serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        h2 {
            font-family: 'Fraunces', serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
        }

        h3, h4, p{
            font-family: 'Outfit', sans-serif;
        }

        button {
            border-radius: 1.5rem !important; 
            background-color: #35564E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important
        }

        button[kind="secondary"] {
            border-radius: 1.5rem !important; 
            background-color: #C9A227 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important
        }

        button[kind="tertiary"] {
            border-radius: 1.5rem !important; 
            background-color: #20342F !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important
        }
        
        button:hover{
            transform: scale(1.05)
        }

        /* Text input styling */
        .stTextInput input {
            background-color: white !important;
            border: 1px solid #C9E2DB !important;
            border-radius: 0.8rem !important;
            color: #20342F !important;
        }

        .stTextInput input::placeholder {
            color: #8FA69E !important;
            opacity: 1 !important;
        }

        h2 {
        font-family: 'Fraunces', serif !important;
        font-size: 2rem !important;
        line-height: 0.9 !important;
        margin-bottom: 0rem !important;
        color: #20342F !important;
        }

        .stTextInput label p,
        .stTextInput label,
        label {
        color: #20342F !important;
        }

        .stApp p, 
        .stApp span, 
        .stApp div[data-testid="stMarkdownContainer"] {
            color: #20342F !important;
        }

        .stApp button, 
        .stApp button * {
            color: white !important;
        }

        /* Global Dialog/Modal Styling — applies to ALL st.dialog popups */
        div[data-testid="stDialog"] div[role="dialog"] {
            background-color: #20342F !important;
            border-radius: 1.5rem !important;
        }

        div[data-testid="stDialog"] h1 {
            color: #EAF3F0 !important;
            font-family: 'Fraunces', serif !important;
        }

        div[data-testid="stDialog"] label,
        div[data-testid="stDialog"] label p,
        div[data-testid="stDialog"] p {
            color: #C9E2DB !important;
        }

        div[data-testid="stDialog"] .stTextInput input {
            background-color: white !important;
            color: #20342F !important;
            border-radius: 0.8rem !important;
        }

        div[data-testid="stDialog"] .stTextInput input::placeholder {
            color: #8FA69E !important;
            opacity: 1 !important;
        }


        </style>
        """,
        unsafe_allow_html=True
    )