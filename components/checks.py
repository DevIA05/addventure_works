# Active to test database connection in streamlit

import streamlit as st

from database.database import sqlRequest, cnxn


def check_database_connection():
    cursor = cnxn.cursor()
    st.title("Check if connection to database")
    version = sqlRequest(cursor, "SELECT @@version;")
    st.text(version)

    st.title("Test database query")
    test = sqlRequest(cursor, "SELECT TOP (10) * FROM DimCurrency;")
    st.text(test)

    cursor.close()
