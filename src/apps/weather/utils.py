from apps.weather.models import City, Forecast
import requests


class WeatherController:
    URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dca5866c7ce15e293544c5154fc22dc6'

    def fetch_all(self):
        cities = City.objects.all()
        if cities.exists():
            for city in cities:
                r = requests.get(self.URL.format(city.name)).json()
                temperature = r['main']['temp']
                description = r['weather'][0]['description']
                icon = r['weather'][0]['icon']
                data = {
                    "city": city,
                    "temperature": temperature,
                    "description": description,
                    "icon": icon,
                }
                print(f"Job: {data}")
                Forecast.objects.create(**data)

    def fetch_one(self, city):
        r = requests.get(self.URL.format(city.name)).json()
        temperature = r['main']['temp']
        description = r['weather'][0]['description']
        icon = r['weather'][0]['icon']
        city_weather = {
            'city': city.name,
            'temperature': temperature,
            'description': description,
            'icon': icon,
        }
        data = {
            "city": city,
            "temperature": temperature,
            "description": description,
            "icon": icon,
        }
        Forecast.objects.create(**data)
        return city_weather
