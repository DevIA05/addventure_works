# chart à tester=>
# st.plotly_chart
# st.pydeck_chart
# st.map

import streamlit as st

from database import sqlRequest

from plots import display_plot_1

st.title("AdventureWorks dashboard")

st.title("Check if connection to database")
version = sqlRequest("SELECT @@version;")
st.text(version)

st.title("Test database query")
test = sqlRequest("SELECT TOP (10) * FROM person.person;")
st.text(test)

display_plot_1()
# st.plotly_chart
