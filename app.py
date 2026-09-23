import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Stock Nodo CBA")

# Conexión a Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(ttl=0)

# Eliminar filas vacías
df = df.dropna(how="all")

# Configurar la columna DN SPARE como imagen
st.dataframe(
    df,
    column_config={
        "DN SPARE": st.column_config.ImageColumn(
            "Vista Previa", help="Foto del repuesto", width="small"
        )
    },
    hide_index=True,
)