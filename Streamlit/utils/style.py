"""Estilização da Página"""
def inject_custom_css():
    import streamlit as st
    st.markdown(
        """
        <style>
        .stApp {
            background-color:#ebeff7; 
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }

        h1, h2, h3 {
            color: #0E1117;
            font-family: 'Segoe UI', sans-serif;
        }

        .css-1d391kg {
            color: #FF4B4B !important;
        }

        .st-emotion-cache-1eyfjps {
            background-color: #c7d4fb!important;
        }

        /* Estilo para o título */
        .st-emotion-cache-10trblm {
            position: absolute !important;
            top: 20px !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            z-index: 1000 !important;
            background-color: #AAB7D5 !important;
            padding: 10px 20px !important;
            border-radius: 10px !important;
        }

        /* Estilo para o conteúdo principal */
        .main .block-container {
            background-color: #cad3e6 !important;
            padding: 2rem !important;
            border-radius: 10px !important;
            margin-top: 2rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
