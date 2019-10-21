import requests

response = requests.get('https://google.com')
print(response.content)
