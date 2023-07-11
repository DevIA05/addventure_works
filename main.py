# chart à tester=>
# st.plotly_chart
# st.pydeck_chart
# st.map

import streamlit as st

from database import sqlRequest

from plots import display_plot_1, display_plot_2, display_plot_3
from checks import check_database_connection

st.title("AdventureWorks dashboard")


# Checks
check_database_connection()

# Tests plots
# display_plot_1()
# display_plot_2()
display_plot_3()
