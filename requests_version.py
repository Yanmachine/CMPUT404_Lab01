import requests

print(requests.__version__)

url = "http://google.com"

res = requests.get(url)

print(res.text)

#code = requests.get("http://google.com/teapot")

#print(code.status_code)
