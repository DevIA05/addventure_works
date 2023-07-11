import streamlit as st

from database.database import sqlRequest, cnxn

from components.checks import check_database_connection
from components.plots import display_turnover_per_months
from components.test_plots import display_plot_1, display_plot_2, display_plot_3


# ------------------PAGE------------------------------------------
st.title("AdventureWorks dashboard")

# Checks
check_database_connection()

# Tests plots
# Carefull=> sql query don't match with DW database
# display_plot_1()
# display_plot_2()
# display_plot_3()

# Plots
display_turnover_per_months()

# cursor.close()
# cnxn.close()
