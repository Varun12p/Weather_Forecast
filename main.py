import streamlit as sd
import plotly.express as px
from backend import get_data

sd.title("Weather Forecast for the next days.")
place = sd.text_input("Place", placeholder="Enter the city.")
days = sd.slider("Forecast Days.", min_value=1, max_value=5,
          help="Select the number of forecasted days")
option = sd.selectbox("Selecet data to view.", ("Temperature","Sky"))

sd.subheader(f"{option} for the next {days} days in {place}.")

if place:
    try:
        filtered_data = get_data(place,days)
        if option == "Temperature":
            temp = [i["main"]["temp"] / 10 for i in filtered_data]
            date = [i["dt_txt"] for i in filtered_data]
            figure = px.line(x=date, y= temp, labels={"x": "Dates", "y": "Temperature (C)"})
            sd.plotly_chart(figure)

        if option == "Sky":
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {'Clear': 'images/clear.png', 'Clouds':'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow':'images/snow.png'}
            image_path = [images[condition] for condition in sky_condition]
            sd.image(image_path, width=120)
    except KeyError:
        sd.write("Place does not exist.")
