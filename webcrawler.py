import requests
from bs4 import BeautifulSoup

def blinds_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.bunnings.com.au/search/products?q=venetian%20blinds&sort=BoostOrder&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)

        # up to 2:35 in video 2.
        # trying to fing unique trait specific to title that we can tell BeautifulSoup to use.        