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
fruits_selected = slit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries', 'Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
slit.dataframe(fruits_to_show)

# New section to display fruityvice api response
slit.header('Fruityvice Fruit Advice!')
fruit_choice = slit.text_input('What fruit would you like information about?','Kiwi')
slit.write('The user entered ', fruit_choice)

import requests as rqst
fruityvice_response = rqst.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pnda.json_normalize(fruityvice_response.json())
slit.dataframe(fruityvice_normalized)




