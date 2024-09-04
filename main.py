import streamlit as sd

sd.title("Weather Forecast for the next days.")
place = sd.text_input("Place", placeholder="Enter the city.")
days = sd.slider("Forecast Days.", min_value=1, max_value=5,
          help="Select the number of forecasted days")
option = sd.selectbox("Selecet data to view.", ("Temperature","Sky"))

sd.subheader(f"{option} for the next {days} days in {place}.")