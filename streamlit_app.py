import streamlit

streamlit.title('Quick Brown Fox')

streamlit.header('🍞Manybe a Menu')
streamlit.text('🥗Omega 2 & Blueberry Oatmeal')
streamlit.text('🥣Kale, spinach & Rocket Sm')
streamlit.text('🥑🍞Hard Boiled Free-Range Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list .set_index('FRuit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
