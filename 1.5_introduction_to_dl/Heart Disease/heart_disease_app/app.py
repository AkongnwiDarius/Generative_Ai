import streamlit as st 
import numpy as np 
import pickle 
import tensorflow as tf 
from tensorflow.keras.models import load_model

#Load the model
model = load_model('Heart_Disease_ann.keras')

#Load the scaler 
# with open('Heart_Disease_inference_kit', 'rb') as file:
#     scaler = pickle.load('scaler_mean')

#Page configuration
st.set_page_config(page_title='Heart Disease Prediction',page_icon='❤️', layout='centered')

#Title
st.title('❤️ Heart Disease Prediction')
st.write('Enter the required information below to get a prediction')