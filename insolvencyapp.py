import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from classification import Prediction

# Setting page configuration
st.set_page_config(page_title = "Insolvency", page_icon = 
":moneybag:", layout="wide")
st.markdown("##")

#---------------------------------------------------------------------------------------------------------------#
#                                                 SIDEBAR SETTINS                                               #
#---------------------------------------------------------------------------------------------------------------#

# Sidebar population
sBox = st.sidebar.selectbox("Menu", ["Home","Manual Entry","Load Data"])

#----------------------------------------- Sidebar options configuration ----------------------------------------

# Function to configure the Overview page specifications


def PageSpecifications(sBox):
    
    # -------------------------------------------------------------------------------------------------------------------------------#
    #                                                     HOME                                                                       #
    # -------------------------------------------------------------------------------------------------------------------------------#

    if sBox == "Home":
        # Setting the page header
        st.markdown("<h1 style='text-align: center; color: black;'> INSOLVENCY </h1>", unsafe_allow_html=True)
        # Adding spaces between the header and image
        st.write()
        st.write()
        #st.title("Cryptocurrency Performance Index")
        imagemain = Image.open("bg1.jpeg")
        st.image(imagemain, caption="Insolvency", width =1000)
        st.markdown("##")
      
        #with col3:
        #    st.write("")


    elif sBox == 'Manual Entry':
        # Setting the page header
        st.markdown("<h1 style='text-align: center; color: black;'> Insolvency Status</h1>", unsafe_allow_html=True)
        st.write('')
        st.markdown("<h5 style='text-align: left; color: black;'> Input Values</h5>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns([3,3,3])
        with c1:
            col1 = st.number_input('Current Liability to Equity')
            col2 = st.number_input('ROA(B) before interest and depreciation after tax')
            col3 = st.number_input('Net profit before tax/Paid-in capital')
            col4 = st.number_input('Inventory and accounts receivable/Net value')
            
        with c2:
            col5 = st.number_input('ROA(A) before interest and \% after tax') 
            col6 = st.number_input('Liability to Equity')
            col7 = st.number_input('Persistent EPS in the Last Four Seasons')

        with c3:             
            
            col8 = st.number_input('ROA(C) before interest and depreciation before interest')
            col9 = st.number_input('Current Liabilities/Equity')
            col10 = st.number_input('Borrowing dependency')


        if st.button('Predict'):
            # Prediction
            result = Prediction([[col1,col2,col3,col4,col5,col6,col7,col8,col9,col10]])
            st.markdown("<h5 style='text-align: left; color: black;'> Prediction </h5>", unsafe_allow_html=True)
            st.success('Prefoction = {}'.format(result))

    #----------------------------------------------------------------------------------------------------------------#
    #                                               LOAD DATA                                                        #
    #----------------------------------------------------------------------------------------------------------------#

    elif sBox == 'Load Data':
        # Setting the page header
        st.markdown("<h1 style='text-align: center; color: black;'> Insolvency Status</h1>", unsafe_allow_html=True)
        st.write('')
        file = st.file_uploader('Upload file', type = ['csv'])
        if file is not None:
            if st.button('Predict'):
                # Prediction
                data = pd.read_csv(file, header=None)
                data_pred = data.iloc[: ,1:].values
                data_pred = list(data_pred)
                result = Prediction(data_pred)
                unique = np.unique(result)
                st.markdown("<h5 style='text-align: left; color: black;'> Prediction </h5>", unsafe_allow_html=True)
                st.success('Classes Detected = {}'.format(unique))

                data.columns = ['Net profit before tax/Paid-in capital', 'ROA(C) before interest and depreciation before interest',
                 'Liability to Equity', 'Current Liabilities/Equity', 'Borrowing dependency', 'Current Liability to Equity',
                 'ROA(B) before interest and depreciation after tax', 'Persistent EPS in the Last Four Seasons', 
                 'Inventory and accounts receivable/Net value', 'ROA(A) before interest and \% after tax', 'Clusters']

                data['Classification'] = result
                data.to_csv('results.csv')
                st.write('')
                with open('results.csv') as f:
                    st.download_button('Download CSV', f)

PageSpecifications(sBox)