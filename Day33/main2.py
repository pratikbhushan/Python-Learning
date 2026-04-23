import requests
import datetime as dt

MY_LAT = 12.971599
MY_LONG = 77.594566

parameters = {
               "lat": MY_LAT,
               "lng": MY_LONG,
               "formatted": 0

}

response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

current_time = dt.datetime.now()
print(current_time.hour)

