import streamlit as st
import pandas as pd

import auth
import logica as lg

auth.generarLogin()
if 'usuario' in st.session_state:
    st.header('Pagina para :blue[Añadir Interaccion]')
    
    # Cargar el DataFrame cada vez que se abre la página
    df = lg.cargar_datos()
    
    # Agregar un selectbox para elegir una fila
    selected_row = st.selectbox('Seleccione una fila:', df.index)

    # Mostrar la fila seleccionada
    st.write('Fila seleccionada:')
    st.write(df.loc[selected_row].to_frame().T)
    
    # Botón para abrir el formulario de detalles del cliente
    with st.form(key='detalle_cliente_form', clear_on_submit=True):
        # Selectboxes para resultado y promesa
        resultado = st.selectbox('Resultado:', ['Atendió cliente', 'Atendió un tercero', 'No localizado'], key='resultado')
        promesa = st.selectbox('Promesa:', ['Si', 'No', 'None'], key='promesa')
        
        # Botón de envío
        submit_button = st.form_submit_button(label='Guardar')
    
        # Lógica de guardado al enviar el formulario
        if submit_button:
            if 'puesto' in st.session_state:
                lg.guardar_datos(selected_row, st.session_state['puesto'], resultado, promesa)
                st.success('Datos guardados exitosamente')
                #st.write("<meta http-equiv='refresh' content='0'>", unsafe_allow_html=True)
                #st.experimental.rerun()  # Recargar la página para actualizar la tabla
            else:
                st.error('Error: puesto no definido en session_state')


