import streamlit as st

from database import sqlRequest


def check_database_connection():
    st.title("Check if connection to database")
    version = sqlRequest("SELECT @@version;")
    st.text(version)

    st.title("Test database query")
    test = sqlRequest("SELECT TOP (10) * FROM DimCurrency;")
    st.text(test)
