import requests

url = "http://127.0.0.1:8000/personal"

response = requests.post(url, json = {"name":"Alexander"})
print(response.json())