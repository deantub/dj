import requests

# Зробити виклик через API та зберегти відповідь.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Зберегти відповідь API у змінну.
response_dict = r.json()

# Обробити результати.
print(response_dict.keys())