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

# TODO: Utiliser les "title" des graphs

# Plots
# Créer une mise en page à deux colonnes
col1, col2 = st.columns(2)
with col1:
    if st.checkbox('Afficher le graphique 1', value=True):
        display_turnover_per_year()
with col2:
    if st.checkbox('Afficher le graphique 2', value=True):
        display_turnover_per_country()
# TODO: Add spinner

if st.checkbox('Afficher le graphique 3', value=True):
    display_nbSale_per_country()
