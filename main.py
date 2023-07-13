import streamlit as st

# from components.checks import check_database_connection
from components.plots import display_turnover_per_country, display_turnover_per_year, \
    display_nbSale_per_country


# Initial page config
st.set_page_config(
    page_title="AdventureWorks",
    layout="wide",
)

# ------------------PAGE------------------------------------------
cola1, cola2, cola3 = st.columns(3)
with cola2:
    st.title("AdventureWorks dashboard")

# Checks
# check_database_connection()


# Plots
# Créer une mise en page à deux colonnes
col1, col2 = st.columns(2)
with col1:
    display_turnover_per_year()
with col2:
    display_turnover_per_country()
# TODO: Add spinner
display_nbSale_per_country()
