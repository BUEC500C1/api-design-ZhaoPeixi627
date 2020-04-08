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

def predict(airport_name):
    dic = read_csv('airports.csv') 
    try:  
        data = wearther_api(dic[airport_name])
        temp = data['main']['temp']
        city = data['name']
        country = data['sys']['country']
        feels_like = data['main']['feels_like']
        result = "The country is:" + str(country) + "\n" + "The city is:" + str(city)  + "\n" + "The temperature of the Airport is:" + str(temp) + "\n"+ "The Temperature feels like:" + str(feels_like)
        return result
    except:
        return "Wrong Input"
    

## test (predict('Fulton Airport'))
## test (predict('General Edward Lawrence Logan International Airport'))