import requests

print(requests.__version__)

code = requests.get("http://google.com/teapot")

print(code.status_code)
