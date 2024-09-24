# Wir benötigen das requests Modul, um HTTP Anfragen zu senden
import json

import requests

# Die BASE URL der Postman-API, die wir verwenden wollen
base_url = "https://postman-library-api.glitch.me"


## Nun können wir HTTP Anfragen an bestimmte Endpoints senden

# GET /books
response = requests.get(base_url + "/books")
# Die Antwort ist im JSON-format, also können wir sie direkt in ein Python Dictionary umwandeln
data = response.json()
# Wir können die Daten auch formatiert ausgeben, um sie im Terminal besser lesbar zu machen
formatted_data = json.dumps(data, indent=2)
print(formatted_data)


# GET /books/:id
book_id = "48v65poqjFpGVm_"
response = requests.get(base_url + "/books/" + book_id)  # Schreib hier deine eigene ID
data = response.json()
formatted_data = json.dumps(data, indent=2)
print(formatted_data)


# POST /books
request_body = {
    "title": "John Doe doesn't have Github",
    "author": "Esma",
    "genre": "drama",
    "yearPublished": 2024,
}

response = requests.post(
    base_url + "/books",
    json=request_body,
    headers={
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Connection": "keep-alive",
    },
)
print("STATUS CODE POST request:", response.status_code)


# PATCH /books/:id
request_body = {
    "checkedOut": True,
}
response = requests.patch(
    base_url + "/books/" + book_id,  # Schreib hier deine eigene ID
    json=request_body,
    headers={
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Connection": "keep-alive",
    },
)
print("STATUS CODE PATCH request:", response.status_code)


# DELETE /books/:id
response = requests.delete(
    base_url + "/books/" + book_id
)  # Schreib hier deine eigene ID
print("STATUS CODE DELETE request:", response.status_code)
