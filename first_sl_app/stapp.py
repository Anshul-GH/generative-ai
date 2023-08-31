import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np


logo = Image.open("images/sample_logo.png")
st.image(logo, width=100)

# st.set_page_config(layout='wide')

st.header('This is a header.')

# dataframe
df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
st.write(df)


# radio button
genre = st.radio(
    "What is your favourite movie genre?",
    ('Comedy', 'Drama', 'Documentary')
)

if genre == "Comedy":
    st.write('You selected Comedy.')
elif genre == "Drama":
    st.write('You selected Drama.')
else:
    st.write('You selected Documentary.')



# charts
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.area_chart(chart_data)
st.line_chart(chart_data)



# containers
container1 = st.container()
container2 = st.container()

container1.write("This is container 1.")
container2.write("This is container 2.")



# user input
user_input = st.text_input("User Input", placeholder="Default text goes here.")

if st.button("Submit"):
    if user_input:
        st.write(user_input)
