# chart à tester=>
# st.plotly_chart
# st.pydeck_chart
# st.map

import streamlit as st

from database import sqlRequest


st.title("AdventureWorks dashboard")

st.title("Check if connection to database")
version = sqlRequest("SELECT @@version;")
st.text(version)

st.title("Test database query")
test = sqlRequest("SELECT TOP (10) * FROM person.person;")
st.text(test)

st.title("Chart test")
# Chart histo employé Homme / Femme / Autre
sexe_chart = sqlRequest(
    "SELECT COUNT(Gender) FROM HumanResources.Employee GROUP BY Gender ORDER BY Gender"
)

sexe_chart_data = []
for elt in sexe_chart:
    for subelt in elt:
        sexe_chart_data.append(subelt)

st.text(sexe_chart)
st.text(sexe_chart_data)

st.bar_chart(sexe_chart_data)
