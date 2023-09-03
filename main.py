import requests
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
config = dotenv_values(".env")
key = os.environ.get("X-RapidAPI-Key")
host = os.environ.get("X-RapidAPI-Host")
print(key)
print(host)
url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": "53.1,-0.13"}

headers = {
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": host
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
