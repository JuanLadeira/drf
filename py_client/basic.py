import requests

endpoint = "https://localhost:8000/"

get_response = requests.get(endpoint, verify=False)
print(get_response.text)
