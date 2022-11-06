import streamlit

streamlit.title('Quick Brown Fox')

streamlit.header('🍞Manybe a Menu')
streamlit.text('🥗Omega 2 & Blueberry Oatmeal')
streamlit.text('🥣Kale, spinach & Rocket Sm')
streamlit.text('🥑🍞Hard Boiled Free-Range Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
