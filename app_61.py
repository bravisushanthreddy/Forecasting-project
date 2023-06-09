#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import pickle
from plotly import graph_objs as go
from pickle import load
import plotly
from statsmodels.tsa.arima.model import ARIMA


# In[3]:


st.title('AAPL Stock Forecasting Using Streamlit')


# In[4]:


st.subheader('Group 1')


# In[5]:


st.subheader('AAPL Dataset')


# In[6]:



df = pd.read_csv("AAPL.csv")
st.write(df)
df.set_index('Date',inplace=True)


# In[7]:



fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index,y=df.Close,name='stock_close'))
fig.layout.update(title_text='Line graph of Close price',xaxis_rangeslider_visible=True)
st.plotly_chart(fig)


# In[8]:


loaded_model = pickle.load(open("model_trained.pkl",'rb'))


# In[9]:


days = st.slider('Days for Prediction',0,200)


# In[10]:


if days > 1:
    fct = pd.DataFrame(loaded_model.forecast(days))
    st.write(fct)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=fct.index,y=fct.predicted_mean,name='Forecast'))
    fig2.layout.update(title_text='Forecast of Closing price for the next given number of days',xaxis_rangeslider_visible=True)
    st.plotly_chart(fig2)

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df.index,y=df.Close,name='original_data'))
    fig3.add_trace(go.Scatter(x=fct.index,y=fct.predicted_mean,name='Forecast'))
    fig3.layout.update(title_text='Displaying forecast along with the original data',xaxis_rangeslider_visible=True)
    st.plotly_chart(fig3)


# In[ ]:




