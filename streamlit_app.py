import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('Mani Yuvi')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

api_res = requests.get('https://fruityvice.com/api/fruit/all')
streamlit.text(api_res.json())
streamlit.dataframe(pandas.json_normalize(api_res.json()))


