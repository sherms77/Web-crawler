# test how to get text from HTML object
# refer to note 281121 in notes.md for analysis

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Soft_drink'

source_code = requests.get(url) # Connects to webpage in url variable and stores results in source_code variable.
# print(source_code) # see output for requests.get()

plain_text = source_code.text # Original code from tutorial - Takes the text from webpage (stuff required to crawl) and stores it in plain_text variable.

# saves output from plain_text to plainHTML.txt
html_file = open('plainHTML.txt', 'w')
html_file.write('THIS IS THE OUTPUT FROM THE PLAIN TEXT VARIABLE: \n')
html_file.write('\n')
html_file.write(plain_text)
html_file.close

soup = BeautifulSoup(plain_text, "html.parser") # Converts text from webpage into a bs4 object and stores in soup variable. Formats it into bs4 format so it can sift through the links.

# saves output from soup to soup.txt
soup_file = open('soupFile.txt', 'w')
soup_file.write('THIS IS THE OUTPUT FROM THE SOUP VARIABLE: \n')
soup_file.write('\n')
soup_file.write(plain_text)
soup_file.close

print('Output saved to plainHTML.txt and soupFile.txt in /home/sherms/Projects/web crawler/tests')