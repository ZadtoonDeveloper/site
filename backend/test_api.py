import requests

url = "http://0.0.0.0:8000"
url1 = "http://0.0.0.0:8000" #"https://sitesitesitesss.herokuapp.com"
#response = requests.post(url1, data = {"name":"Alexander"})
#print(response.json())
def make_request(url, request):
    response = requests.post(url, json = request)
    return response.text
def make_get_post(url):
    response = requests.get(url)
    return response.content

def many_functions():
    print(make_request(url1 + '/personal', {"name" : "Alex"}))
    print(make_request(url1 + '/area-triangle-90', {"a" : 4, "b" : 5}))
    print(make_request(url1 + '/area-rectangle', {"a": 4, "b": 5}))
    print(make_get_post(url1 + '/'))
    print(make_get_post(url1 + '/datetime'))
print(make_request(url1 + '/personal', {"name" : "Alex"}))
#print(make_get_post(url1 + '/datetime'))
#many_functions()