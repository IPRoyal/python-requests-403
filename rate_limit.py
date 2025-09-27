import requests
import time

url = 'https://example.com'

for _ in range(5):
    response = requests.get(url)
    print(response.status_code)
    time.sleep(2)  # wait 2 seconds between requests
