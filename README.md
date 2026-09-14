# AQI Analysis

A Python-based project for analyzing Air Quality Index (AQI) and pollutant levels using real-time air quality data.

## Project Overview

This project uses Python to fetch air quality data for a user-specified city through an API. The data is processed to obtain AQI and pollutant concentrations, and the AQI is categorized into different air-quality levels.

The project also provides health and environmental suggestions based on the AQI category and visualizes AQI observations using Matplotlib.

## Technologies Used

- Python
- Requests
- Geopy
- Matplotlib
- OpenWeatherMap API

## Features

- Accepts a city name as input
- Converts the city name into geographical coordinates
- Fetches real-time air quality data through an API
- Extracts AQI and pollutant levels
- Categorizes air quality
- Provides health and environmental suggestions
- Visualizes AQI variation using a graph

## Project Workflow

City Name  
↓  
Geocoding  
↓  
Latitude & Longitude  
↓  
API Request  
↓  
AQI & Pollutant Data  
↓  
AQI Categorization  
↓  
Health & Environmental Suggestions  
↓  
Visualization

## Pollutants Analyzed

- CO — Carbon Monoxide
- NO₂ — Nitrogen Dioxide
- O₃ — Ozone
- SO₂ — Sulfur Dioxide
- PM2.5
- PM10
- NH₃ — Ammonia

## Learning Outcomes

Through this project, I practiced:

- Working with APIs
- Processing JSON data
- Geocoding
- Data extraction and manipulation
- Conditional logic
- Data visualization using Matplotlib
- Working with real-time data

## Future Improvements

- Store AQI observations in a structured dataset
- Perform statistical analysis of pollutant levels
- Compare AQI across multiple cities
- Add interactive visualizations
- Develop a simple dashboard
