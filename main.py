import streamlit as st
from database import sqlRequest

st.title("AdventureWorks dashboard")

st.title("Check if connection to database")
version = sqlRequest("SELECT @@version;")
st.text(version)

st.title("Test database query")
test = sqlRequest("SELECT TOP (10) * FROM person.person;")
st.text(test)
