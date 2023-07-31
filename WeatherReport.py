# importing requests and json
import requests, json

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = input("Enter city name : ")
API_KEY = "a0f99fe4edfe0ce0d96575335fe75996"

# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# HTTP request
response = requests.get(URL)

# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']

   # getting temperature
   temperature = main['temp']

   print(f"{CITY:-^30}")
   print(f"Temperature: {round(temperature - 273.15 ,  2)} °C")
else:
   # showing the error message
   print("Error in the HTTP request")
   print("We are unable to fetch data of your city please Check Your Spelling or Choose Another City")