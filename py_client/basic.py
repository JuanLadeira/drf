import requests

endpoint = "https://localhost:8000/api/"

get_response = requests.get(endpoint, verify=False)
print(get_response.text)
print(get_response.status_code)
print(get_response.json())
