import os
import requests
import pandas as pd
from pydantic import BaseModel
from sqlalchemy import create_engine
from dotenv import load_dotenv

# .env file se variables load karna
load_dotenv()

# Environment variable se API key uthana
API_KEY = os.getenv("OPENWEATHER_API_KEY")  
CITIES = ["Karachi", "Lahore", "Islamabad", "London", "Tokyo", "Turkey"]

# 2. UPDATED PYDANTIC MODEL (Wind speed aur Pressure ke sath)
class WeatherData(BaseModel):
    city: str
    temperature: float
    humidity: int
    wind_speed: float
    pressure: int
    weather_condition: str

# A. EXTRACT & TRANSFORM
raw_data_list = []

for city in CITIES:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Pydantic se validate aur structure karna
        validated_data = WeatherData(
            city=data["name"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            pressure=data["main"]["pressure"],
            weather_condition=data["weather"][0]["description"]
        )
        
        raw_data_list.append(validated_data.dict())
    else:
        print(f"Failed to fetch data for {city}. Status code: {response.status_code}")

# Check karein ke data aaya hai ya nahi
if len(raw_data_list) > 0:
    df = pd.DataFrame(raw_data_list)
    print("\n--- Transformed Data (With Wind Speed & Pressure) ---")
    print(df)

    # B. LOAD (SQLite Database me Save Karna)
    engine = create_engine('sqlite:///weather_data.db')
    df.to_sql('city_weather', con=engine, if_exists='replace', index=False)

    print("\nData successfully loaded into 'weather_data.db'!")
else:
    print("\nError: No data was fetched. Please check your API key!")