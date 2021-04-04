import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://forecast.weather.gov/MapClick.php?lat=34.1016&lon=-118.3371'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather_stuff = pd.DataFrame({
    'period': period_names,
    'short_descriptions': short_description,
    'temperatures': temperatures,
})

weather_stuff.to_csv('weather.csv')
