import requests

def get_weather(key, city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": key,
        "units": "metric" 
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to retrieve weather information. Status code: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("No weather data to display.")

def main():
    key = "0aff935b7dd282eff6475e5a2634ad96"  
    city = input("Enter the city name: ")

    weather_data = get_weather(key, city)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
