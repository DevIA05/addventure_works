import streamlit as st

import pandas as pd
from database import sqlRequest


def display_turnover_per_months():
    st.title("Turnover per months")

    turnover_data = sqlRequest(
        "SELECT SUM(UnitPrice) AS Sales , YEAR(OrderDate) as YearOfSale \
        FROM AdventureWorksDW2019.dbo.FactInternetSales \
        GROUP BY YEAR(OrderDate) ORDER by YearOfSale"
    )
    df = pd.DataFrame(turnover_data)
    st.text(turnover_data)
    print(df)
