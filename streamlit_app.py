import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('Quick Brown Fox')

streamlit.header('🍞Manybe a Menu')
streamlit.text('🥗Omega 2 & Blueberry Oatmeal')
streamlit.text('🥣Kale, spinach & Rocket Sm')
streamlit.text('🥑🍞Hard Boiled Free-Range Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#Create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


#New Section to display Fruityvice api reposnse 
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
      back_from_frunction = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_frunction)
except URLError as e:
    streamlit.error()

#don't run anything past here while we troubleshoot
streamlit.stop()

streamlit.header("The Fruit load list contains:")
#Snowflake-related frunctions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from FRUIT_LOAD_LIST")
      return my_cur.fetchall()
    
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

#This will not work correctly, but just go with it for now
my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
