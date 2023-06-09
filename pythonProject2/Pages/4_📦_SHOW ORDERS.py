import streamlit as st
import mysql.connector
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid
from h import dbconnection

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image : url("https://assets-global.website-files.com/6009ec8cda7f305645c9d91b/6010843e4702bd1918217200_6002086f72b727e1b701d3df_blog-image.jpeg")
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()

mydb, mycursor = dbconnection()
st.header("Order Details")
query=("select * from CUST_ORDERS")
mycursor.execute(query)
df = pd.DataFrame(mycursor)
df = df.rename(columns={0: 'ORDER_ID',1:'PRODUCT CATEGORY',2:'FROM CITY', 3:'TO CITY',4:'0RDER_DATE',5:'SHIPPED_DATE',6:'ORDDER STATUS',7:'CUSTOMER ID'})

gb = GridOptionsBuilder.from_dataframe(df)

gridoptions = gb.build()

AgGrid(
    df,
    gridOptions=gridoptions
)