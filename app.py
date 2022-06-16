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


