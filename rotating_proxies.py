import requests
from itertools import cycle

proxies = [
    'http://10.10.1.10:3128',
    'https://10.10.1.11:1080'
]
proxy_pool = cycle(proxies)

url = 'https://example.com'

for _ in range(5):
    proxy = next(proxy_pool)
    response = requests.get(url, proxies={"http": proxy, "https": proxy})
    
    if response.status_code == 200:
        print('Success!')
    else:
        print(f'Failed with status code: {response.status_code}')
