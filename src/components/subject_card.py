import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left: 8px solid #35564E; padding:25px; border-radius: 20px; border: 1px solid #C9E2DB; margin-bottom:20px;">
        <h3 style="margin:0; color: #20342F; font-size: 1.5rem ">{name}</h3>
        <p style="color:#5C7A72; margin:10px 0;">Code : <span style="background:#EAF3F0; color:#35564E; padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #EAF3F0; padding:5px 12px; border-radius:12px; font-size:0.9rem; color:#35564E;">{icon} <b>{value}</b> {label} </div>'
        
        html+= "</div>"
    st.markdown(html, unsafe_allow_html=True)
    if footer_callback:
        footer_callback()