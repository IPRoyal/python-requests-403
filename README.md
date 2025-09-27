# Solving 403 Forbidden Errors in Python Requests

---

## Why 403 errors?
A `403 Forbidden` error means the server understood the request but refuses to authorize it. It is one of the most common issues in web scraping with Python Requests.

---

## Common Causes
- **Authentication errors**: page is behind login or requires special authorization.  
- **User-agent restrictions**: many websites block the default Python Requests UA.  
- **IP address blocking**: your IP is blacklisted or restricted.  
- **Rate limiting**: too many requests in a short time.  
- **Anti-bot systems**: advanced detection beyond simple headers.  

---

## Strategies with examples

### 1. Switch User-Agent
*Many sites block the default Requests UA. Pretend to be a browser instead.*
```python
import requests

url = 'https://iproyal.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('Success!')
else:
    print(f'Failed with status code: {response.status_code}')
```

---

### 2. Use Rotating Proxies
*If banned by IP, switch proxies to continue scraping.*
```python
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
```

---

### 3. Implement Rate Limiting
*Slow down requests to avoid triggering simple anti-bot filters.*
```python
import requests
import time

url = 'https://example.com'

for _ in range(5):
    response = requests.get(url)
    print(response.status_code)
    time.sleep(2)  # wait 2 seconds between requests
```

---

### 4. Use a Headless Browser
*For tougher anti-bot measures or JavaScript-heavy sites, fall back to Selenium.*
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get('https://iproyal.com')

content = driver.page_source
print(content)

driver.quit()
```

---

## Tips & Best Practices
- Rotate both **user agents** and **proxies** together for stronger evasion.  
- Always **add delays** to avoid simple rate-limit bans.  
- If scraping at scale, implement **retry logic** in addition to rate limiting.  
- Use Selenium or another headless browser only when Requests alone fails (it is heavier and slower).  
- Remember: authentication-protected pages still require valid credentials; these strategies don’t bypass logins.  

---

## Final Thoughts
There is no single solution for all 403 errors. Often, you’ll need to **combine strategies** (e.g., change user agent, add rate limiting, and rotate proxies) for reliable scraping. For highly protected websites, switching to a headless browser may be unavoidable.

These techniques help you continue scraping without being blocked, while respecting target sites by reducing load and avoiding aggressive request patterns.

