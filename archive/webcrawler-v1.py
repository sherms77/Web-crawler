from os import name
import requests # Requests module requests info from a webpage - connects to the webpage.
from bs4 import BeautifulSoup # BeautifulSoup4 pulls data out of HTML and XML files.

# blinds_spider function - core spider to crawl pages
def blinds_spider(max_pages): # max pages paramater sets how many pages to crawl
    page = 1 # Count initializer
    
    # While loop to crawl pages based on argument passed to page paramater.
    while page <= max_pages: # while value in page is less than max pages execute loop
        url = 'https://www.bunnings.com.au/search/products?q=venetian%20blinds&sort=BoostOrder&page=' + str(page) # url to crawl. Value from page counter converted to string and added to end of the url to specify page number on site to be crawled.
        source_code = requests.get(url) # Connects to webpage in url variable and stores results in source_code variable.
        print(url) # prints url that its trying to access
        print(source_code) # see output for requests.get()
        
        plain_text = source_code.text # Takes the text from webpage (stuff required to crawl) and stores it in plain_text variable.
        soup = BeautifulSoup(plain_text, "html.parser") # Converts text from webpage into a bs4 object and stores in soup variable. Formats it into bs4 format so it can sift through the links.

        # for loop loops through all the source code and picks out the links with the class specified below.
        # refer to uniqueClass.html for info about class.
        for link in soup.findAll('a', {'class': 'Anchor__styledAnchor-sc-1gq32ow-0 SearchProductTilestyle__SearchProductTileWrapper-sc-7jrh24-2 eePBcM ghAMXK product-tile-main-wrapper'}): # unique identifier
            href = 'https://www.bunnings.com.au' + link.get('href') # Builds out the url for the product.
            print(href)
            name = link.string # Takes string from within the <a> tags and saves it in name.
            print(name) # Prints the product names
        page += 1

# 181121: up to 8:14 in video 2
# 181121: debugged it - cannot access url on line 10. Get response 403 error - forbidden client.
# 181121: see if there is work around for 403 error or use another url.

# print('test output')

blinds_spider(1)