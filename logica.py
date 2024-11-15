import pandas as pd

# Ruta del archivo CSV
CSV_FILE_PATH = './data/df.csv'

# Cargar datos desde el archivo CSV
def cargar_datos():
    df = pd.read_csv(CSV_FILE_PATH)
    df.set_index('Solicitud_id', inplace=True)
    df = df[df['Atendido'] == 0]
    return df

def cargar_datosCliente(index):
    df = cargar_datos()
    df = df.loc[[index]]
    columns_to_select = ['Numero_tlf', 'Direccion']
    atraso = {
        'atraso_1_29': 'Atraso de 1 mes',
        'atraso_30_59': 'Atraso de 2 meses',
        'atraso_60_89': 'Atrsa de 3 meses',
        'atraso_90_119': 'Atraso de 4 meses',
        'atraso_120_149': 'Atraso de 5 meses',
        'atraso_150_179': 'Atraso de 6 meses',
        'atraso_180_más': 'Ataso de 7 meses o más',
    }
    Total_Interecciones = len(eval(df.at[index, 'Interacciones']))
    interacciones = eval(df.loc[index, 'Interacciones'])
    Ultima_Interaccion = interacciones[-1] if Total_Interecciones > 0 else None
    atraso = df['Nivel_Atraso'].map(atraso).loc[index]

    existing_columns = [col for col in columns_to_select if col in df.columns]
    new_df = df[existing_columns]
    new_df['Total Interacciones'] = Total_Interecciones
    new_df['Ultima Interaccion'] = Ultima_Interaccion
    new_df['Nivel Atraso'] = atraso
    return new_df

def mostrar_datosPaP():
    df = cargar_datos()
    columns_to_select = ['Numero_tlf', 'Direccion', 'Interacciones']
    existing_columns = [col for col in columns_to_select if col in df.columns]
    new_df = df[existing_columns]
    return new_df

def mostrar_datosCC():
    df = cargar_datos()
    columns_to_select = ['Numero_tlf', 'Interacciones']
    existing_columns = [col for col in columns_to_select if col in df.columns]
    new_df = df[existing_columns]
    return new_df

def mostrar_datosAE():
    df = cargar_datos()
    columns_to_select = ['Numero_tlf', 'Interacciones']
    existing_columns = [col for col in columns_to_select if col in df.columns]
    new_df = df[existing_columns]
    return new_df

# Función para guardar datos en el archivo CSV
def guardar_datos(row, tp, resultado, promesa):
    # Mapear el tipo de gestión
    tipo_gestion_map = {
        'PaP': 'Gestión Puerta a Puerta',
        'CC': 'Call Center',
        'AE': 'Agencias Especializadas'
    }
    tp = tipo_gestion_map.get(tp, tp)
    
    # Nueva interacción
    nueva_interaccion = {
        'Tipo_Gestión': tp,
        'Resultado': resultado,
        'Promesa_Pago': promesa
    }
    
    # Cargar datos actuales
    df = cargar_datos()
    
    # Convertir la cadena JSON a una lista de diccionarios
    interacciones = eval(df.at[row, 'Interacciones'])
    
    # Añadir la nueva interacción
    interacciones.append(nueva_interaccion)
    
    # Convertir la lista de diccionarios de nuevo a una cadena JSON
    df.at[row, 'Interacciones'] = str(interacciones)

    # Cambiar la variable Atendido de 0 a 1
    df.at[row, 'Atendido'] = 1
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(CSV_FILE_PATH, index=True)


def añadir_incidencia(selected_row, incidencia):
    df = cargar_datos()
    
    # Convertir la cadena JSON a una lista de incidencias
    incidencias = eval(df.at[selected_row, 'Incidencia']) if 'Incidencia' in df.columns and pd.notna(df.at[selected_row, 'Incidencia']) else []
    
    # Añadir la nueva incidencia
    incidencias.append(incidencia)
    
    # Convertir la lista de incidencias de nuevo a una cadena JSON
    df.at[selected_row, 'Incidencia'] = str(incidencias)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(CSV_FILE_PATH, index=True)

def mostrar_incidencia(selected_row):
    df = cargar_datos()
    incidencias = eval(df.at[selected_row, 'Incidencia'])
    return '\n\rIncidencia: '.join([f"{i+1}. {incidencia}" for i, incidencia in enumerate(incidencias)])