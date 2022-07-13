import requests

endpoint = "www.google.com"

get_response = requests.get(endpoint, verify=False, retries=False)
print(get_response.text)
print(get_response.status_code)
print(get_response.json())
