import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
from model_price import *

#  Header and Text
st.write("""

# Predict Price of Your Car

My name is **Bassem Ahmed Ahmed Mokhtar Eldeghady**, Thats End to End Machine Learning Project Here you can  predict the price of your car.

This Project based on  **Python** only

""")

# Css Code for Design
st.markdown(""" <style>
.css-ffhzg2{background-image: url("https://images.pexels.com/photos/11159145/pexels-photo-11159145.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-repeat: no-repeat;
background-size: cover;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style> """, unsafe_allow_html=True)

# import images
Mitsubishi = Image.open('Mitsubishi.jpeg')
audi = Image.open('Audi.jpeg')
Mercedes = Image.open('Mercedes.jpeg')
pmw = Image.open('pmw.jpeg')
Toyota = Image.open('Toyota.jpeg')
Renault = Image.open('Renault.jpeg')

# Text for fill the data
st.write('')
st.write('Please Fill The Following to Predict The Price OF Your Car')
st.write('')

# Display Images
co1, co2, co3 = st.columns(3)
with co1:
    st.image(Mitsubishi, width = 200)
with co2:
    st.image(audi, width = 200)
with co3:
    st.image(Mercedes, width = 200)
st.write('')

co1, co2, co3 = st.columns(3)
with co1:
    st.image(pmw, width = 200)
with co2:
    st.image(Toyota, width = 200)
with co3:
    st.image(Renault, width = 200)
st.write('')

# Enter the Model
Model = st.text_input('Model', '')
st.write('')

# Enter another Feature
col1, col2 = st.columns(2)
with col1:
    Brand = st.selectbox('Brand',  ['', 'BMW', 'Mercedes-Benz', 'Audi', 'Toyota','Mitsubishi', 'Renault'])
    if Brand:
        st.write('Your cas is : ', Brand)
with col2:
    Type = st.selectbox('Type', ['', 'sedan', 'van', 'crossover', 'vagon', 'other', 'hatch'])
    if Type:
        st.write('Type of your car is : ', Type)
st.write('')

col3, col4 = st.columns(2)
with col3:
    Color = st.selectbox('Color', ['', 'Black', 'Blue', 'Red', 'Gold', 'White', 'other'])
    if Color:
        st.write('Color of Your Car is : ', Color)
with col4:
    Engine_Type = st.selectbox('Engine Type', ['', 'Petrol', 'Diesel', 'Gas', 'Other'])
    if Engine_Type:
        st.write('Your Engine Type of Your Car is : ', Engine_Type)
st.write('')


registered = st.radio('Is Your Car Registered ? ', ('Yes', 'No'), 1)
if registered == 'Yes':
    st.write('Your Car is Registered')
    Registered = 1
else:
    st.write('Your Car is not Registered')
    Registered = 0
st.write('')

Year = st.slider('Year', 1970, 2024, 1997)
if Year:
    st.write('Your Car is Made in : ', Year)
st.write('')

Mileage = st.slider('Mileage',0, 980, 490)
if Mileage:
    st.write('Mileage of Your Car is : ', Mileage)
st.write('')
try:
    col_, col_1, col_2 = st.columns(3)
    with col_:
        st.write('')
    with col_1:

        if st.button('Predict'):
            st.write('Price : {0} $'.format( round(user_end(Year, Mileage, 'Brand_'+ Brand, 'Body_'+Type,  'Engine Type_' + Engine_Type, Registered)[0][0], 3) ))
    with col_2:
        st.write('')
except:
        st.write('There are One or more Filed Empty You should Fill all Requried Data')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
