import streamlit as st

from database.database import sqlRequest, cnxn

from components.checks import check_database_connection
from components.plots import display_turnover_per_country, display_turnover_per_year

# from components.test_plots import display_plot_1, display_plot_2, display_plot_3
# Initial page config
st.set_page_config(
    page_title="AdventureWorks",
    layout="wide",
)

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
    # Créer une mise en page à deux colonnes
    col1, col2 = st.columns(2)
    with col1:
        display_turnover_per_year()
    with col2:
        display_turnover_per_country()
# cursor.close()
# cnxn.close()
