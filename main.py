import requests
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse
#weather API key
import os

vonage_api_key = os.environ.get("VONAGE_API_KEY")
vonage_api_secret = os.environ.get("VONAGE_API_SECRET")
weather_api_key = os.environ.get("WEATHER_API_KEY")
private_number = os.environ.get("PRIVATE_NUMBER")
vonage_number= os.environ.get("VONAGE_NUMBER")
Weather_API_Endpoint = "https://api.weatherapi.com/v1/forecast.json"
MY_LAT = 40.71427
MY_LON =-74.00597
MY_CITY="New York City,NY"

parameters ={
    "key":weather_api_key,
    "q": MY_CITY,
    "days": 1
}

response=requests.get(Weather_API_Endpoint,params=parameters)
print(response.text)
weather_data=response.json()
weather_codes_next_12_hours=[]
hourly_weather_list=weather_data["forecast"]["forecastday"][0]["hour"]

for i in hourly_weather_list[0:12]:
    weather_codes_next_12_hours.append(i["condition"]["code"])

rainy_if=1063

rain=False

for i in weather_codes_next_12_hours:
    if i>=rainy_if:
        rain=True

if rain:
    client = Vonage(Auth(api_key=vonage_api_key, api_secret=vonage_api_secret))
    message = SmsMessage(
        to=private_number,
        from_=vonage_number,
        text="Bring an Umbrella",
    )
    response: SmsResponse = client.sms.send(message)
    print(response)
