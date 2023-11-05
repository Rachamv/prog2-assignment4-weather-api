import json
import urllib.request

map_city_to_coords = {
    'Abuja': 'lat=9.0764785&lon=7.398574',
    'Nairobi': 'lat=-1.2920659&lon=36.8219462',
    'Accra': 'lat=5.6037168&lon=-0.1869644',
    'Lagos': 'lat=6.5244&lon=3.3792',
    'Tokyo': 'lat=35.6895&lon=139.6917',
    'Paris': 'lat=48.8566&lon=2.3522',
    'London': 'lat=51.5074&lon=-0.1278',
    'New York': 'lat=40.7128&lon=-74.0060',
    'Sydney': 'lat=-33.8688&lon=151.2093',
    'Moscow': 'lat=55.7558&lon=37.6176',
    'Rio de Janeiro': 'lat=-22.9068&lon=-43.1729',
    'Beijing': 'lat=39.9042&lon=116.4074',
    'Cairo': 'lat=30.0330&lon=31.2336',
    'Berlin': 'lat=52.5200&lon=13.4050',
    'Rome': 'lat=41.9028&lon=12.4964',
    'Bangkok': 'lat=13.7563&lon=100.5018',
    'Madrid': 'lat=40.4168&lon=-3.7038',
}


def interpret_wind_direction(direction):
    direction_mapping = {
        'N': 'from the north',
        'NE': 'from the northeast',
        'E': 'from the east',
        'SE': 'from the southeast',
        'S': 'from the south',
        'SW': 'from the southwest',
        'W': 'from the west',
        'NW': 'from the northwest'
    }
    return direction_mapping.get(direction, 'from an unknown direction')

def interpret_wind_speed(speed):
    if speed < 0.3:
        return "Calm"
    elif 0.3 <= speed < 3.4:
        return "Light"
    elif 3.4 <= speed < 8.0:
        return "Moderate"
    elif 8.0 <= speed < 10.8:
        return "Fresh"
    elif 10.8 <= speed < 17.2:
        return "Strong"
    elif 17.2 <= speed < 24.5:
        return "Gale"
    elif 24.5 <= speed < 32.6:
        return "Storm"
    else:
        return "Hurricane"




def show_weather_to_user(weather_data_list):
    for weather_data in weather_data_list:
        hour_number = weather_data['timepoint']
        temperature = weather_data['temp2m']
        wind_speed = weather_data['wind10m']['speed']
        descriptive_wind_speed = interpret_wind_speed(wind_speed)
        wind_direction = weather_data['wind10m']['direction']
        descriptive_wind_direction = interpret_wind_direction(wind_direction)
        print(f'On hour {hour_number},')
        if hour_number == 24:
            print('(in one day)')
        elif hour_number == 48:
            print('(in two days)')
        elif hour_number == 72:
            print('(in three days)')

        print(f'The temperature is {temperature}°C and the wind is approaching at {wind_speed}m/s '
              f'({descriptive_wind_speed}) {descriptive_wind_direction}')


def show_weather():
    city_name = input('Please type a city: ').capitalize()
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        api_response = get_api_results(city_name)
        all_data = json.loads(api_response)
        weather_data_list = all_data['dataseries']
        show_weather_to_user(weather_data_list)


def get_api_results(city):
    coords = map_city_to_coords[city]
    url = ('https://www.7timer.info/bin/astro.php?' +
        f'{coords}&ac=0&unit=metric&output=json')
    results = urllib.request.urlopen(url)
    json_content = results.read().decode('utf-8')
    return json_content

show_weather()
