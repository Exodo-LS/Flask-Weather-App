import requests
from flask import Blueprint, render_template, current_app, request, url_for, abort
from app.temperature_forecast.forms import weather_form
from werkzeug.utils import redirect
from jinja2 import TemplateNotFound
from flask_login import login_required

forecast = Blueprint('forecast', __name__, template_folder='templates')


@forecast.route('/temperature_forecast', methods=['GET', 'POST'])
@login_required
def get_temperature():
    form = weather_form()
    if form.validate_on_submit():
        if request.method == "POST":
            city = request.form['city']
            api_key = current_app.config.get('OPENWEATHER_API_KEY')

            weather_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},&units=imperial'
            weather_data = requests.get(weather_url).json()
            print(weather_data)
            temp = weather_data.get('main', {}).get('temp')
            feel = weather_data.get('main', {}).get('feels_like')
            cast = weather_data.get('weather')[0].get('main')
            desc = weather_data.get('weather')[0].get('description')
            icon = weather_data.get('weather')[0].get('icon')
            humidity = weather_data.get('main', {}).get('humidity')
            wind_speed = weather_data.get('wind', {}).get('speed')
            lat = weather_data.get('coord', {}).get('lat')
            lon = weather_data.get('coord', {}).get('lon')

            return render_template('result.html', temp=temp, feel=feel, cast=cast, desc=desc, icon=icon, humidity=humidity, wind_speed=wind_speed, lat=lat, lon=lon, city=city)
    try:
        return render_template('temperature_forecast.html', form=form)
    except TemplateNotFound:
        abort(404)
