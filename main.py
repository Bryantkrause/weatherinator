import requests
from dotenv import load_dotenv, dotenv_values
import os
import pandas as pd

load_dotenv()
config = dotenv_values(".env")
key = os.environ.get("X-RapidAPI-Key")
host = os.environ.get("X-RapidAPI-Host")
datalist = []
url = "https://weatherapi-com.p.rapidapi.com/history.json"

querystring = {
    		
            "q": "San Diego",
            "dt": "2023-09-01"
			   }

headers = {
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": host
}

response = requests.get(url, headers=headers, params=querystring)
print(response)
data = response.json()

datalist.append(data['forecast']['forecastday'])

newdatalist = datalist[0][0]
# print(data)
# data2 = data.text
df = pd.json_normalize(data)
# df = pd.DataFrame(newdatalist)
# df = pd.read_json(data2)
# df = pd.read_json(data)

pd.DataFrame(data).to_csv('out.csv',index=False)