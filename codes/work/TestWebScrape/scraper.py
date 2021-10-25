# webscraping behind a login
from bs4 import BeautifulSoup  as bs                   # requires beautifulsoup4 & lxml parser
import requests

# Load webpage content
url = requests.get('https:fxxxx')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36', 'Origin': 'https://auth.conquestcyber.com', 'Referer': 'https://auth.conquestcyber.com/'}

# going to use request to create a sessions object - this sessions going to hold a lot of data we get back
s = requests.sessions()

session_code = s.get(url).session['session_code']
