import Streamlit

Streamlit.title('my parent healthy denner')


Streamlit.header('🥣 Breakfast Menu')
Streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
Streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
Streamlit.text('🥑 Hard-Boiled Free-Range Egg')
Streamlit.text('🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

