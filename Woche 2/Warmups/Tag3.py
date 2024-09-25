"""
Führe einen request auf folgende URL aus: https://jsonplaceholder.typicode.com/posts
Gib aus den Daten eine Liste mit den Namen der Objekte zurück.

Zusatzaufgabe:
Gib gemeinsam mit dem Namen zusätzlich die ID der Objekte aus.
"""

import requests


def get_posts(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        posts = []
        for post in data:
            posts.append({"title": post["title"], "id": post["id"]})

        return posts
    else:
        raise Exception("Error: Could not get posts")


posts = get_posts("https://jsonplaceholder.typicode.com/posts")
print(posts)
