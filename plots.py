import streamlit as st

import pandas as pd
from database import sqlRequest

import plotly.graph_objects as go
import plotly.express as px

from utils import getConfig


def display_bar_chart(x, y):
    # Use textposition='auto' for direct text
    fig = go.Figure(
        data=[
            go.Bar(
                x=x,
                y=y,
                text=y,
                textposition="auto",
            )
        ]
    )

    st.plotly_chart(fig, use_container_width=True)


def display_turnover_per_months():
    st.title("Turnover per months")

    turnover_data = sqlRequest(
        "SELECT SUM(UnitPrice) AS Sales , YEAR(OrderDate) as YearOfSale \
        FROM "
        + getConfig("DATABASE")
        + ".dbo.FactInternetSales \
        GROUP BY YEAR(OrderDate) ORDER by YearOfSale"
    )
    st.text(turnover_data)
    y = []
    x = []

    for elt in turnover_data:
        # print(elt)
        y.append(elt[1])
        x.append(float(elt[0]))

    print("x", x)
    print("y", y)
    df = pd.DataFrame(dict(x=y, y=x))
    # Mettre en place request sql pour récup valeur max pour la range_y
    fig = px.line(df, x="x", y="y", title="Unsorted Input", range_y=[0, 10000000])
    # fig = px.bar(df, x="x", y="y", title="Unsorted Input")
    st.plotly_chart(fig, use_container_width=True)
    # print(df)
