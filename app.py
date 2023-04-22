import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageEnhance
df=pd.read_csv(r"cleaned.csv")


st.set_page_config(page_title="Pub App",
                   page_icon=":🍾:",
                   layout="centered")

#Background Image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://wallpapercave.com/wp/Rk1SlMI.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title(":blue[Our Pubs App 🍺🍻]")

st.markdown("## :red[About the Dataset]")

st.markdown("###### :red[Top Five Rows of Dataset]")
st.write(df.head())

st.markdown("###### :red[Total Numbers of Rows and Columns]")
st.write(":red[Total number of Pubs:]", df.shape[0])
st.write(":red[Total number of columns:]", df.shape[1])

st.write(":red[This app allows you to find pubs in the United Kingdom (UK) and discover their locations.]")
st.write(f':red[We have :blue[{len(df)}] pub locations in our database.]')
st.write("- :red[Number of unique local authorities:]", df["local_authority"].nunique())
st.write("- :red[Number of unique postal codes:]", df["postcode"].nunique())
st.write(f':red[max latitude value=:blue[60.764969] and min latitude value=:blue[49.892485]]')
st.write(f':red[max longitude value=:blue[1.757763] and min longitude value=:blue[-7.384525]]') 