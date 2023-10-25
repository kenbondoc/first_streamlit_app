import streamlit as slit
slit.title('My Parents New Healthy Diner')
slit.header('BreakFast Menu')
slit.text('🥣 Omega 3 & Blueberry Oatmeal')
slit.text('🥗 Kale, Spinach & Rocket Smoothie')
slit.text('🐔 Hard-Boiled Free-Range Egg')
slit.text('🥑🍞 Avocado Toast')
slit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pnda
my_fruit_list = pnda.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
slit.dataframe(my_fruit_list)
