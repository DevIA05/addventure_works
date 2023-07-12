# Contains chart to display

# TODO: Replacer les cursor.close()
import streamlit as st

import numpy as np
import pandas as pd
from database.database import sqlRequest

import plotly.express as px
import plotly.graph_objects as go

from database.utils import getConfig
from database.database import cnxn, database

from .utils import Geocoder
import pydeck as pdk


# Autres graphs:


def display_turnover_per_year():
    cursor = cnxn.cursor()
    st.title("Turnover per year")

    turnover_data = sqlRequest(
        cursor,
        "SELECT SUM(UnitPrice) AS Sales , YEAR(OrderDate) as YearOfSale \
        FROM "
        + database
        + ".dbo.FactInternetSales \
        GROUP BY YEAR(OrderDate) ORDER by YearOfSale",
    )

    y = []
    x = []

    for elt in turnover_data:
        y.append(elt[1])
        x.append(float(elt[0]))

    df = pd.DataFrame(dict(x=y, y=x))
    df.rename(columns={"x": "Year"}, inplace=True)
    df.rename(columns={"y": "Turnover"}, inplace=True)

    sorted_x_array = np.sort(np.array(x))
    sorted_x_list = sorted_x_array.tolist()

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
        + database
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
        new_rows.append({"country": country, "turnover": turnover})

    # Ajouter les nouvelles lignes au DataFrame
    df = pd.DataFrame(new_rows)

    # Créer les données pour le diagramme en secteurs
    labels = df["country"]
    values = df["turnover"]

    # Créer l'objet Pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    st.plotly_chart(fig, use_container_width=True)

    cursor.close()
# MAP --------------------------------------------------------------------------
def display_nbSale_per_country():
    cursor = cnxn.cursor()
    st.title("Quantité d'ordre passé dans le Pays")

# Requête 
# Table
# o DimSalesTerritory
# o FactInternetSales
# - Somme le nombre de TotalQuantity par SalesTerritoryCountry
# Car pour un même pays, il peut y avoir plusieurs TerritoryKey
# Exemple: United State: 1 - Northwest
#                        2 - Northest    
# -- Récupère le nom de pays SalesTerritoryCountry en fonction du TerritoryKey
# --- Somme le nombre de OrderQuantity (TotalQuantity) par TerritoryKey

    sperc_data = sqlRequest(
        cursor,
        "SELECT SUM(nbSByC.TotalQuantity), nbSByC.SalesTerritoryCountry \
        FROM ( "
            "SELECT nbSByT.TotalQuantity, ST.SalesTerritoryCountry \
            FROM ( \
                SELECT SUM(OrderQuantity) as TotalQuantity , SalesTerritoryKey \
                FROM "
                + getConfig("DATABASE")
                + ".dbo.FactInternetSales \
                GROUP BY SalesTerritoryKey) as nbSByT," 
            + getConfig("DATABASE")
            + ".dbo.DimSalesTerritory as ST\
            WHERE nbSByT.SalesTerritoryKey = ST.SalesTerritoryKey \
            ) as nbSByC \
        GROUP BY nbSByC.SalesTerritoryCountry"
    )
    cursor.close()
# Transformation de la liste de vecteur en dataframe    
    # print(sperc_data)
    df = pd.DataFrame.from_records(sperc_data, columns=['TotalQuantity', 
                                                        'SalesTerritoryCountry'])
    # print(df)

# Coordonnées
    geocoder = Geocoder()
    df[['latitude', 'longitude']] = df['SalesTerritoryCountry'].apply(
        lambda x: pd.Series(geocoder.get_coordinates(x))
    )
    print(df)

# Rendu de la carte 
    # max = df['TotalQuantity'].max()
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=df['latitude'].mean(),
            longitude=df['longitude'].mean(),
            zoom=0.5,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ColumnLayer',
                data=df,
                get_position=['longitude', 'latitude'],
                get_elevation='TotalQuantity',
                elevation_scale=200,
                radius=100000,
                get_fill_color=[200, 30, 0, 160],
                #get_fill_color=lambda row: geocoder.get_color(row, max),
            ),
            # pdk.Layer(
            #     'TextLayer',
            #     data=df,
            #     get_position=['longitude', 'latitude'],
            #     get_text='TotalQuantity',
            #     get_color=[0, 0, 0],
            #     get_size=250,
            #     get_alignment_baseline="'bottom'",
            # )
        ],
    ))
