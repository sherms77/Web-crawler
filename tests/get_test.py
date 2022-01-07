# test request.get() on site with no 403 error
import requests

url = 'https://en.wikipedia.org/wiki/Soft_drink' # 203 response
# url = 'https://www.bunnings.com.au/search/products?q=venetian%20blinds&sort=BoostOrder&page=' # 403 response
# url = 'https://www.bunnings.com.au/zone-interiors-50mm-vermont-timber-venetian-blind_p0027232' # 403 response


site_request = requests.get(url)
print(site_request) # prints outcome of get request

link = str(url) # converts url to a string
print(link) # prints url as a link