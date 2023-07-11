import streamlit as st

from database.database import sqlRequest, cnxn

from components.checks import check_database_connection
from components.plots import display_turnover_per_year
from components.test_plots import display_plot_1, display_plot_2, display_plot_3


# ------------------PAGE------------------------------------------
st.title("AdventureWorks dashboard")

checks_tab, plots_tab = st.tabs(["Checks", "Plots"])

# Checks
with checks_tab:
    check_database_connection()

# Tests plots
# Carefull=> sql query don't match with DW database
# display_plot_1()
# display_plot_2()
# display_plot_3()

# Plots
with plots_tab:
    display_turnover_per_year()

# cursor.close()
# cnxn.close()
