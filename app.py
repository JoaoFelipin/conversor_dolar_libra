import requests
import json

endpoint_url = 'https://cdn.jsdelivr.net/gh/prebid/currency-file@1/latest.json?date=20240129'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

response = requests.get(endpoint_url, headers=headers)
json_data = response.json()
