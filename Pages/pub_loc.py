import streamlit as st
import pandas as pd
from PIL import Image, ImageEnhance

df=pd.read_csv(r"cleaned.csv")

# Load home page image
img = Image.open('img-1.jpg')
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.5)

st.image(img)

location_type = st.selectbox(
    "Select the location type:",
    ('Postal Code', 'Local Authority'))

if location_type == 'Postal Code':
    location = st.selectbox('Select the Postal Code:', df['postcode'].unique())
    pubs = df[df['postcode'] == location].reset_index()
else:
    location = st.selectbox('Select Local Authority:', df['local_authority'].unique())
    pubs = df[df['local_authority'] == location].reset_index()
st.write(f'We found {len(pubs)} pubs in {location}.')

st.table(pubs[['name','address']])

st.map(pubs[['latitude', 'longitude']])