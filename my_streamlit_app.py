import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# CONFIGURATION PAGE
st.set_page_config(layout = 'wide')

# DATAFRAME
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# TTIRES
st.title('Semaine 11 : Quête Streamlit')
st.write("by Caroline Cornelus")


## SIDEBAR avec FILTRE REGION
with st.sidebar:
    # liste des filtres
    regions = ['All'] + list(df_cars['continent'].unique())
    
    # création du selectbox
    region_button = st.selectbox('REGION', regions)

    # conditions : avec ou sans filtre
    if region_button == 'All':
        df_region = df_cars
    else:
        df_region = df_cars[df_cars['continent'] == region_button]



# ONGLETS
tab1, tab2, tab3,tab4 = st.tabs(["Dataframe", "Correlation", "Histogramme", "Scatterplot"])


#### ONGLET 1 : DATAFRAME ####
with tab1:
    tab1.header("Dataframe Cars")
    tab1.dataframe(df_region)

    
    
#### ONGLET 2 : CORRELATION ####
with tab2:
    tab2.header("Graphique de Corrélation")

    # Analyse
    with tab2.expander("Correlation : explication"):
            st.write(f'''Région All :

Il y a une forte corrélation positive entre cylinders, cubicinches, hp, weight lbs

Il y a une forte corrélation négative entre mpg et cylinders/ cubicinches / hp / weight lbs 
    ''')
    # Graph    
    plt.subplots(figsize = (4,4))
    df_numeric = df_region.select_dtypes('number')
    viz_correlation = sns.heatmap(df_numeric.corr(), 
                          annot = True,
                          center = 0,
                          cmap = sns.color_palette("vlag", as_cmap=True)
                         )
    viz_correlation.set_title(f'Corrélation (région : {region_button})')
    tab2.pyplot(viz_correlation.figure, use_container_width = False)

    
    
#### ONGLET 3 : HISTOGRAMME ####
with tab3:
    tab3.header("Histogramme 'Weight'")

    # Analyse
    with tab3.expander("Histogramme : explication"):
        st.write(f'''Région All :
        
La majorité des voitures pèse entre 1900 et 2300 pounds.

Très peu de voiture pèse au dessus de 4600 pounds''')
    
    # Graph
    plt.subplots(figsize = (5,2))
    viz_histogramme = sns.histplot(df_region['weightlbs'])
    viz_histogramme.set_title(f'Histogramme (région : {region_button})')
    tab3.pyplot(viz_histogramme.figure, use_container_width = False)



#### ONGLET 4 : SCATTERPLOT ####
with tab4:
    tab4.header("Scatterplot")
    
    # Analyse
    with tab4.expander("Scatterplot : explication"):
        st.write(f'''à suivre...''')

    # Graph
    plt.subplots(figsize = (5,2))
    viz_scatterplot = sns.scatterplot(df_region, x = 'hp', y = 'cubicinches')
    viz_scatterplot.set_title(f'Scatterplot (région : {region_button})')
    tab4.pyplot(viz_scatterplot.figure, use_container_width = False)
    
    
    


