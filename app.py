from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
OPENWEATHERMAP_API_KEY = 'YOUR_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    location = request.form.get('location')
    q=f'{location},usa'
    if location:
        # Make a request to the OpenWeatherMap API to get weather data
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={q}&appid={b88cc12bb7fbe1e3980d1218fe79de72
}&units=metric'
        print(url)
        response = requests.get(url)
        data = response.json()
        if data.get('list'):
            # Extract weather data for the next 7 days
            daily_weather = data['list'][:7]
            return render_template('weather.html', location=location, daily_weather=daily_weather)
        else:
            return render_template('error.html', message='Unable to fetch weather data')
    else:
        return render_template('error.html', message='Please provide a location')

if __name__ == '__main__':
    app.run(debug=True)
