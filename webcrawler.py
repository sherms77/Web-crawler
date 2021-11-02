import requests
from bs4 import BeautifulSoup

def blinds_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.bunnings.com.au/search/products?q=venetian%20blinds&sort=BoostOrder&page=' + str(page)
        source_code = requests.get(url)
        

        