import streamlit as st
import auth

auth.generarLogin()
if 'usuario' in st.session_state:
    st.header('Página para :red[Añadir Aviso]')

    incidencia = st.text_area("Añadir incidencia:")
    if st.button("Enviar"):
        st.write(f"Incidencia añadida: {incidencia}")