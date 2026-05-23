from django.shortcuts import render
import requests

def home(request):

    weather_data = {}
    error = ""

    if request.method == "POST":

        city = request.POST.get('city')

        api_key = "f1a7de72cedd7264c1bec2c5743b2f67"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)

        data = response.json()

        if data.get("cod") != 200:

            error = "City not found. Please enter a valid city name."

        else:

            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed'],
                'description': data['weather'][0]['description']
            }

    return render(request, 'index.html', {
        'weather_data': weather_data,
        'error': error
    })