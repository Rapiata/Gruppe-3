import requests

BASE_URL = "https://realpython.github.io/fake-jobs/"
response = requests.get(BASE_URL)


print(response.text)
