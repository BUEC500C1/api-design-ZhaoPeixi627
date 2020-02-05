import requests
from pprint import pprint
import pandas as pd

def read_csv(csv):
    airports = pd.read_csv(csv, engine='python', encoding='utf-8')
    name = airports['name']
    municipality = airports['municipality']
    dic = {}
    for i in range(len(airports)):
        dic[name[i]] = municipality[i]
    return dic

def wearther_api(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=69026bebc14e1f98bbed466694ad6e0d'.format(city)
    res = requests.get(url)
    data = res.json()
    return data

def wearther_forecast(city):
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid=d9a49454aeb2886b10005199e720a833'.format(city)
    res = requests.get(url)
    data = res.json()
    return data    

def main(): 
    airport_name = input('Enter a airport: ')
    dic = read_csv('airports.csv')   
    data = wearther_api(dic[airport_name])
    temp = data['main']['temp']
    city = data['name']
    country = data['sys']['country']
    timezone = data['timezone']
    feels_like = data['main']['feels_like']
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    print('The Country of the Airport is:',country)
    print('The City of the Airport is:',city)
    print('The Latitude of the City is:',lat)
    print('The Longtitude of the City is:',lon)
    print('The Timezone of the city:',timezone)
    print('The Temperature of the Airport is:',temp)
    print('The Temperature feels like:',feels_like)
    forecast = wearther_forecast(dic[airport_name])
    print('The Weather Forecast of next 5 days(every three hours):')
    pprint(forecast['list'])

if __name__ == "__main__":
    main()
