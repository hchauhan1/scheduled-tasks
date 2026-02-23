import requests
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse
#weather API key
import os

vonage_api_key = os.environ.get("VONAGE_API_KEY")
vonage_api_secret = os.environ.get("VONAGE_API_SECRET")
weather_api_key = os.environ.get("WEATHER_API_KEY")
Weather_API_Endpoint = "https://api.weatherapi.com/v1/forecast.json"
MY_LAT = 40.71427
MY_LON =-74.00597
MY_CITY="Denver,CO"

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
        to="14093007428",
        from_="19789864299",
        text="Bring an Umbrella",
    )
    response: SmsResponse = client.sms.send(message)
    print(response)

# df=pd.read_csv("weather_conditions.csv")
# weather_data=df.to_dict("records")
# for i in weather_data:
#     print(f"{i["code"], i["day"], i["night"]}\n")


# OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
# appid="65db29743cacbbf3b6af1dd448ca3407"
#
# weater_params={
#     "lat:": MY_LAT,
#     "lon:": MY_LON,
#     "appid:": appid,
#     "cnt":4
# }
# response=requests.get(OWM_Endpoint,params=weater_params)
# response.raise_for_status()
# print(response.status_code)
# data1=response.json()
