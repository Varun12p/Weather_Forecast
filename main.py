import streamlit as sd
import plotly.express as px
from streamlit import plotly_chart

sd.title("Weather Forecast for the next days.")
place = sd.text_input("Place", placeholder="Enter the city.")
days = sd.slider("Forecast Days.", min_value=1, max_value=5,
          help="Select the number of forecasted days")
option = sd.selectbox("Selecet data to view.", ("Temperature","Sky"))

sd.subheader(f"{option} for the next {days} days in {place}.")

date = ["2024-04-12", "2024-04-13","2024-04-14"]
temp = [12,13,14]
figure = px.line(x=date, y= temp, labels={"x": "Dates", "y": "Temperature (C)"})
sd.plotly_chart(figure)
