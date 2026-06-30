import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/2")

print(response.status_code)
print(response.json())