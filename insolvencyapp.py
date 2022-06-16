from calendar import c
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from classification import Prediction
from streamlit_option_menu import option_menu

# Setting page configuration
st.set_page_config(page_title = "Insolvency", page_icon = 
":moneybag:", layout="wide")
st.markdown("##")

#---------------------------------------------------------------------------------------------------------------#
#                                                 SIDEBAR SETTINS                                               #
#---------------------------------------------------------------------------------------------------------------#

# Sidebar population
# sBox = st.sidebar.selectbox("Menu", ["Home","Manual Entry","Load Data"])

with st.sidebar:
    sBox = option_menu(menu_title= 'Menu', options=['Home','Load Data', 'Manual Entry'], 
    icons =['house','book','boxes'],menu_icon='cast', default_index=1)


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
        c1,c2,c3 = st.columns([1,5,1])

        with c1:
            st.write()
        with c2:

            imagemain = Image.open("bg1.jpeg")
            st.image(imagemain, caption="Insolvency", width =750)
            st.markdown("##")
        with c3:
            st.write('')

        c1,c2,c3 = st.columns([1,5,1])
        with c1:
            st.write('')
        with c2:
            st.markdown('''*An organization's ability to learn, and translate that learning into an action
            rapidly, is the ultimate competitive advantage.*''')
        with c3:
            st.write('')
        

        c1,c2,c3 = st.columns([3,5,1])
        with c1:
            st.write('')
        with c2:
            st.markdown('''*Jack Welch (Former CEO of General Electric)*''')
        with c3:
            st.write('')


    elif sBox == 'Manual Entry':
        # Setting the page header
        st.markdown("<h1 style='text-align: center; color: black;'> Insolvency Status</h1>", unsafe_allow_html=True)
        st.write('')
        st.markdown("<h5 style='text-align: left; color: black;'> Input Values</h5>", unsafe_allow_html=True)

        c1, c2, c3, c4,c5 = st.columns([3,3,3,3,3])
        with c1:
            col1 = st.number_input('Current Liability to Equity', 0.0, 1.0)
            col2 = st.number_input('ROA(B) before interest and depreciation after tax', 0.0, 1.0)
            col3 = st.number_input('Net profit before tax/Paid-in capital', 0.0, 1.0)
            col4 = st.number_input('Inventory and accounts receivable/Net value', 0.0, 1.0)
            # col1 = st.slider('Current Liability to Equity', 0.1,1.0,0.5)
            # col2 = st.slider('ROA(B) before interest and depreciation after tax',  0.1,1.0,0.5)
            # col3 = st.slider('Net profit before tax/Paid-in capital',  0.1,1.0,0.5)
            # col4 = st.slider('Inventory and accounts receivable/Net value',  0.1,1.0,0.5)
        with c2:
            st.write('')
        with c3:
            col5 = st.number_input('ROA(A) before interest and \% after tax', 0.0, 1.0) 
            col6 = st.number_input('Liability to Equity', 0.0, 1.0)
            col7 = st.number_input('Persistent EPS in the Last Four Seasons', 0.0, 1.0)
            # col5 = st.slider('ROA(A) before interest and \% after tax',  0.1,1.0,0.5)
            # col6 = st.slider('Liability to Equity',  0.1,1.0,0.5)
            # col7 = st.slider('Persistent EPS in the Last Four Seasons',  0.1,1.0,0.5)
        with c4:             
            st.write('')
        with c5:
            col8 = st.number_input('ROA(C) before interest and depreciation before interest', 0.0, 1.0)
            col9 = st.number_input('Current Liabilities/Equity', 0.0, 1.0)
            col10 = st.number_input('Borrowing dependency', 0.0, 1.0)
            # col8 = st.slider('ROA(C) before interest and depreciation before interest',  0.1,1.0,0.5)
            # col9 = st.slider('Current Liabilities/Equity',  0.1,1.0,0.5)
            # col10 = st.slider('Borrowing dependency',  0.1,1.0,0.5)
             
            


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
