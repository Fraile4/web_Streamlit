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
    client_df = lg.cargar_datosCliente(selected_row)

    # Mostrar la foto correspondiente a la fila seleccionada y la fila en formato vertical en paralelo
    col1, col2 = st.columns(2)

    with col1:
        foto_path = f"data/Fotos/{df.loc[selected_row, 'Foto']}"
        st.image(foto_path, caption='Foto del cliente', width=300)

    with col2:
        #st.write('**Fila seleccionada:**')
        for column in client_df.columns:
            st.write(f"\n{column}: {client_df.at[selected_row, column]}")

    if st.session_state['puesto'] != 'PaP':
        if st.button('Mandar SMS'):
            st.info('SMS enviado exitosamente')
    
    # Botón para abrir el formulario de detalles del cliente
    with st.form(key='detalle_cliente_form', clear_on_submit=True):
        # Selectboxes para resultado y promesa
        resultado = st.selectbox('Resultado:', ['Atendió cliente', 'Atendió un tercero', 'No localizado'], key='resultado')
        promesa = st.selectbox('Promesa:', ['Si', 'No', 'None'], key='promesa')
        
        # Botón de envío
        submit_button = st.form_submit_button(label='Guardar')

        # Mostrar advertencia si 'Incidencia' no está vacía
        if df.loc[selected_row, 'Incidencia'] != '[]':
            st.warning(f"Incidencia: {lg.mostrar_incidencia(selected_row)}")
    
        # Lógica de guardado al enviar el formulario
        if submit_button:
            if 'puesto' in st.session_state:
                lg.guardar_datos(selected_row, st.session_state['puesto'], resultado, promesa)
                st.success('Datos guardados exitosamente')
                #st.write("<meta http-equiv='refresh' content='0'>", unsafe_allow_html=True)
                #st.experimental.rerun()  # Recargar la página para actualizar la tabla
            else:
                st.error('Error: puesto no definido en session_state')


