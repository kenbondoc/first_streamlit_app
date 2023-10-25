import streamlit as slit
slit.title('My Parents New Healthy Diner')
slit.header('BreakFast Menu')
slit.text('🥣 Omega 3 & Blueberry Oatmeal')
slit.text('🥗 Kale, Spinach & Rocket Smoothie')
slit.text('🐔 Hard-Boiled Free-Range Egg')
slit.text('🥑🍞 Avocado Toast')
slit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
# Display the table on the page.
import pandas as pnda
my_fruit_list = pnda.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
my_fruit_list = slit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
slit.dataframe(fruits_to_show)



