import streamlit as st

from database import sqlRequest

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go


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
    st.title("Chart test 2")

    long_df = px.data.medals_long()
    print(long_df)

    fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")

    st.plotly_chart(fig, use_container_width=True)

    st.title("Chart test 3")
    # data = {"Homme": [10], "Femme": [20]}
    data = {"Sexe": ["Homme", "Femme"], "Valeurs": ["20", "10"]}
    df = pd.DataFrame(data)

    fig2 = px.bar(df)
    st.plotly_chart(fig2, use_container_width=True)


def display_plot_3():
    st.title("third attempt")

    sexe_chart = sqlRequest(
        "SELECT COUNT(Gender) FROM HumanResources.Employee GROUP BY Gender ORDER BY Gender"
    )

    sexe_chart_data = []
    for elt in sexe_chart:
        for subelt in elt:
            sexe_chart_data.append(subelt)

    x_data = ["Femme", "Homme"]
    y_data = sexe_chart_data

    # Use textposition='auto' for direct text
    fig = go.Figure(
        data=[
            go.Bar(
                x=x_data,
                y=y_data,
                text=y_data,
                textposition="auto",
                # marker_color="indianred",
            )
        ]
    )

    # fig.show()
    st.plotly_chart(fig, use_container_width=True)
