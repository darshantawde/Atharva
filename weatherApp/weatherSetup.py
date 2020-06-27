import requests

while True:

    city = input('Enter the city:')
    city = list(city)
    city[0] = city[0].upper()
    city = ''.join(city)
    print()

    try:
        query = 'q=' + city
        response = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
        w_data = response.json()
        temperature = w_data['main']['temp']
        temperature = float(temperature)
        temperature = temperature * 1.8 + 32
        wind = w_data['wind']['speed']
        description = w_data['weather'][0]['description']
        weather = w_data['weather'][0]['main']
        print("{}'s temperature: {}°C ".format(city, temperature))
        print("Wind speed: {} m/s".format(wind))
        print("Description: {}".format(description))
        print("Weather: {}".format(weather))
    except:
        print('City name not found...\n')
