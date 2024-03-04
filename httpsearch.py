import requests         # pip install requests


response = requests.get('https://www.youtube.com')
print(response.ok)
