import requests
API_KEY = '1c9dbd438aa9277363a9b656cd0b89a4'
cityName = input('Enter the name of the City: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={API_KEY}'

response = requests.get(url)
# print(response)

if response.status_code == 200:
    weather_data =response.json( )
    weather_disc=weather_data['weather'] [0] ['description']
    temp=weather_data['main']['temp'] -273.15
    # print(weather_disc)
    # Display weather info
    print(f'Weather in {cityName} : {round(temp,2)} C with {weather_disc}')
else:
    print(f'CityName is not found or other issues')