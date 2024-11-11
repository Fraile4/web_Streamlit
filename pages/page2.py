import streamlit as st

import auth
import logica as lg

auth.generarLogin()
if 'usuario' in st.session_state:
    st.header('Página para :red[Añadir Incidencia]')

    df = lg.cargar_datos()
    selected_row = st.selectbox('Seleccione una fila:', df.index)

    incidencia = st.text_area("Añadir incidencia:")
    if st.button("Enviar"):
        st.write(f"Incidencia añadida: {incidencia}")
        lg.añadir_incidencia(selected_row, incidencia)