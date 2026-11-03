# Project 1: ETL + EDA Pipeline (Weather Data)

## Project Overview
This project extracts real-time weather data (including temperature, humidity, wind speed, and pressure) for major cities using the free OpenWeather API. It validates and transforms the data using Pydantic and Pandas, then loads it into a local SQLite database. Finally, an Exploratory Data Analysis (EDA) is performed to generate comparative summary statistics and visual charts using Matplotlib and Seaborn.

## Project Structure
- `main.py`: ETL Pipeline script (Extracts weather metrics, validates via Pydantic, and loads into SQLite).
- `eda.py`: Exploratory Data Analysis script (Generates statistical summaries and 4 comparative visual charts for temp, humidity, wind speed, and pressure).
- `weather_data.db`: SQLite database containing the structured weather data.
- `weather_eda_analysis.png`: Generated EDA multi-plot visualization chart.

## How to Run
1. Install requirements: `pip install requests pandas pydantic sqlalchemy matplotlib seaborn`
2. Run ETL pipeline: `python main.py`
3. Run EDA analysis: `python eda.py`