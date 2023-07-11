# Contains chart to display

import streamlit as st

import pandas as pd
from database.database import sqlRequest

import plotly.express as px

from database.utils import getConfig


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

    # print("x", x)
    # print("y", y)
    df = pd.DataFrame(dict(x=y, y=x))

    # TODO: Mettre en place request sql pour récup valeur max pour la range_y
    fig = px.line(df, x="x", y="y", title="Unsorted Input", range_y=[0, 10000000])
    st.plotly_chart(fig, use_container_width=True)
