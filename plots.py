import streamlit as st

from database import sqlRequest


def display_plot_1():
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


def display_plot_2():
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
