import streamlit as st
import pandas as pd

import auth
import menu
import logica as lg

# Configuración de la página
st.set_page_config(
    page_title="Dimex", 
    page_icon="./favicon.ico"  
)

st.title(':green[Dimex]')

if 'usuario' not in st.session_state:
    st.header(':orange[Login]')
    auth.generarLogin()
else:
    if st.session_state['usuario'] == 'admin':
        st.header(':orange[Registrar]')
        auth.generarRegistro()
    else:
        if st.session_state['puesto'] == 'PaP':
            st.header('Página de :orange[Gestión Puerta a Puerta]')
            st.subheader('Clientes del día:')
            st.write(lg.mostrar_datosPaP())
        elif st.session_state['puesto'] == 'CC':
            st.header('Página de :orange[Call Center]')
            st.subheader('Clientes del día:') 
            st.write(lg.mostrar_datosCC())
        elif st.session_state['puesto'] == 'AE':
            st.header('Página de :orange[Agencias Especializadas]')
            st.subheader('Clientes del día:')
            st.write(lg.mostrar_datosAE())

        #st.header('Página :orange[principal]')
        menu.generarMenu(st.session_state['usuario'])

        ''''''
        