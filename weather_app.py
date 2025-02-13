import streamlit as st
import requests
from datetime import datetime

# Function to get weather data
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Streamlit app
def main():
    st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")
    
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
            font-family: 'Arial', sans-serif;
        }
        h1 {
            color: #1f77b4;
            text-align: center;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: None;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🌤️ Weather App")
    
    api_key = "4311755e70a94a283d4853b9aaed19c5"  # Your API key here
    city = st.text_input("Enter the name of any city", "")
    
    if st.button("Get Weather"):
        if city:
            weather_data = get_weather(api_key, city)
            
            if weather_data.get("cod") != 200:
                st.error("City not found!")
            else:
                temp = weather_data["main"]["temp"]
                weather = weather_data["weather"][0]["description"]
                humidity = weather_data["main"]["humidity"]
                wind_speed = weather_data["wind"]["speed"]
                
                
                st.markdown(
                    f"""
                    <div style="background-color: #e0f7fa; padding: 10px; border-radius: 5px; margin-top: 20px;">
                        <h2 style="color: #00796b;">{city.capitalize()}</h2>
                        <p><strong>Temperature:</strong> {temp}°C</p>
                        <p><strong>Weather:</strong> {weather.capitalize()}</p>
                        <p><strong>Humidity:</strong> {humidity}%</p>
                        <p><strong>Wind Speed:</strong> {wind_speed} m/s</p>
                        
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.error("Please enter a city name.")
            
if __name__ == "__main__":
    main()
