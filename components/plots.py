# Contains chart to display

import os
import streamlit as st

import numpy as np
import pandas as pd
from database.database import sqlRequest

import plotly.express as px
import plotly.graph_objects as go

from database.utils import getConfig
from database.database import cnxn

# Autres graphs:


def display_turnover_per_year():
    cursor = cnxn.cursor()
    st.title("Turnover per year")

    turnover_data = sqlRequest(
        cursor,
        "SELECT SUM(UnitPrice) AS Sales , YEAR(OrderDate) as YearOfSale \
        FROM "
        + os.environ["DATABASE_NAME"]
        + ".dbo.FactInternetSales \
        GROUP BY YEAR(OrderDate) ORDER by YearOfSale",
    )
    # st.text(turnover_data)
    y = []
    x = []

    for elt in turnover_data:
        # print(elt)
        y.append(elt[1])
        x.append(float(elt[0]))

    # print("x", type(x[0]))
    # print("y", y[0])
    df = pd.DataFrame(dict(x=y, y=x))
    df.rename(columns={"x": "Year"}, inplace=True)
    df.rename(columns={"y": "Turnover"}, inplace=True)

    sorted_x_array = np.sort(np.array(x))
    sorted_x_list = sorted_x_array.tolist()
    # fig = px.line(
    #     df, x="x", y="y", title="Unsorted Input", range_y=[0, sorted_x_list[-1]]
    # )
    fig = px.bar(
        df,
        range_y=[0, sorted_x_list[-1]],
        title="",
        x="Year",
        y="Turnover",
        text_auto=True,
    )
    st.plotly_chart(fig, use_container_width=True)

    cursor.close()

def display_turnover_per_country():
    cursor = cnxn.cursor()
    st.title("Turnover per country")
    returned_data = sqlRequest(
        cursor,
        "SELECT t.SalesTerritoryCountry, SUM(s.SalesAmount) AS TotalSalesAmount FROM "
        + getConfig("DATABASE") 
        + ".dbo.DimSalesTerritory t \
            JOIN FactInternetSales s ON t.SalesTerritoryKey = s.SalesTerritoryKey \
            GROUP BY t.SalesTerritoryCountry\
            ORDER BY TotalSalesAmount DESC",
    )

    # Créer une liste pour stocker les nouvelles lignes
    new_rows = []

    # Parcourir les données retournées
    for e in returned_data:
        country = e[0]
        turnover = e[1]

        # Ajouter une nouvelle ligne à la liste
        new_rows.append({'country': country, 'turnover': turnover})

    # Ajouter les nouvelles lignes au DataFrame
    df = pd.DataFrame(new_rows)

    # Créer les données pour le diagramme en secteurs
    labels = df['country']
    values = df['turnover']

    # Créer l'objet Pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    st.plotly_chart(fig, use_container_width=True)

    cursor.close()