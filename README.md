# api-design-ZhaoPeixi627
api-design-ZhaoPeixi627 created by GitHub Classroom
# User's Story
As user, I can get the information of the current weather of the city where the airport locate.
As user, I can get the information of the weather forecast of the city in 5 days every 3 hours.
# Instruction
## Import
Pandas
pprint
requests
## Get API
I use two API.
The first one is to get the current weather by current weather data API.

![image](https://github.com/BUEC500C1/api-design-ZhaoPeixi627/blob/master/data/weather_api.png)
The second API I use is that 5 day/ 3 hour forecast.

![image](https://github.com/BUEC500C1/api-design-ZhaoPeixi627/blob/master/data/5days3hours.png)
## Steps
1. User input a airport's name.
2. Refer the airport's name to the city name in CSV file.
3. Connect current weather data API to get the information of current weather.
4. Connect 5 day/ 3 hour forecast API to get the information of forecast weather.
# Result
User inputs an airport name and get the information of some basic information.

![image](https://github.com/BUEC500C1/api-design-ZhaoPeixi627/blob/master/data/airports.png)
User gets information of the forecast weather.

![image](https://github.com/BUEC500C1/api-design-ZhaoPeixi627/blob/master/data/weather_forecast.png)
