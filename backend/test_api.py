import requests

url = "http://127.0.0.1:8000"
url1 = "https://sitesitesitesss.herokuapp.com"
#response = requests.post(url1, data = {"name":"Alexander"})
#print(response.json())
def make_request(url, request):
    response = requests.post(url, json = request)
    return response.json()
def make_get_post(url):
    response = requests.get(url)
    return response.json()
#print(make_request(url1 + '/personal', {"name" : "Alex"}))
print(make_get_post(url1 + '/datetime'))