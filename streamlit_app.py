import streamlit

streamlit.title('My Parents New Healty Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
file_link = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_fruit_list = pandas.read_csv(file_link)
streamlit.dataframe(my_fruit_list)
