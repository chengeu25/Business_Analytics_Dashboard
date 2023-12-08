import requests

url =  
parameters = {
    "api_key": "YOUR_API_KEY",
    "query": "sales",
    "limit": 5
}

response = requests.get(url, params=parameters)

