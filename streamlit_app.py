import streamlit as slit
import pandas as pnda
import requests as rqst
import snowflake.connector as sf
from urllib.error import URLError

# import streamlit as slit
slit.title('My Parents New Healthy Diner')
slit.header('BreakFast Menu')
slit.text('🥣 Omega 3 & Blueberry Oatmeal')
slit.text('🥗 Kale, Spinach & Rocket Smoothie')
slit.text('🐔 Hard-Boiled Free-Range Egg')
slit.text('🥑🍞 Avocado Toast')
slit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
# Display the table on the page.
# import pandas as pnda
my_fruit_list = pnda.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = slit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries', 'Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
slit.dataframe(fruits_to_show)

# create a repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = rqst.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pnda.json_normalize(fruityvice_response.json())
    return(fruityvice_normalized)

# New section to display fruityvice api response
# import requests as rqst
slit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = slit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    slit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(this_fruit_choice)
    slit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()

slit.stop()

# Snowflake connector
# import snowflake.connector as sf
my_cnx = sf.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
slit.header("The fruit load list contains:")
slit.dataframe(my_data_row)

# Allow end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit') ")



