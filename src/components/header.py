import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/sdHhMNRC/logo.jpg"
    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items:center; justify-content: center; margin-bottom: 30px; margin-top:30px">
            <img src = "{logo_url}" style="height: 100px; border-radius:20px"/>
            <h1 style = 'text-align:center; color:#EAF3F0'>CLASS MARK </h1>        
        </div>
        """,
        unsafe_allow_html=True
    )

def header_dashboard():

    logo_url ="https://i.ibb.co/sdHhMNRC/logo.jpg"   
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px; border-radius:15px' />
            <h2 style='text-align:left; color:#35564E'>CLASS<br/>MARK</h2>
        </div>   
                
                """, 
                unsafe_allow_html=True
    )