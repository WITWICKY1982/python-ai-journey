import requests
post_id = int(input("ENTER POST ID"))

response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

print(response.status_code)
print(response.json())


