import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    data = response.json() # otomatis menjadi dictionary
    print("Title", data["title"])
    print("Body", data["body"])
else:
    print("Error", response.status_code)