import requests
from twilio.rest import Client

lat = 42.733883
lon = 25.485830
endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "bdac3f28d5a5fc8a9607d927c7c8a3f7" #your TWILIO_AUTH_TOKEN
sid = 'ACa03b28b40f29b5954bcf061e3326ae15' #your TWILIO_ACCOUNT_SID
auth_token = '11897332b6a6d1c034160087597eae27'

params = {
    "lat": 64.213547,
    "lon": 27.740135,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(endpoint, params=params)
response.raise_for_status()
weather_data = response.json()
weather = (weather_data["hourly"][:12])

it_will_rain = False
for n in weather:
    condition_code = n["weather"][0]["id"]
    if int(condition_code) < 700:
        it_will_rain = True

if it_will_rain:
    client = Client(sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain!",
        from_='+15736523102', #Your Twilio phone number
        to='Your number' #Only Verified Numbers
    )
    print(message.status)
