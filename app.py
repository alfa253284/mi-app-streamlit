import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Stock Nodo CBA")

url = "https://docs.google.com/spreadsheets/d/1NL2BRRxNlLBL2DJK63DtjLuFDMnbYfHiVktK4pziMSE/edit?gid=0#gid=0"

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url, ttl=0)

st.dataframe(
    df,
    column_config={
        "DN SPARE": st.column_config.ImageColumn("Foto"),
        "Link WhatsApp": st.column_config.LinkColumn(
            "WhatsApp",
            display_text="Enviar a WhatsApp"
        )
    }
)
