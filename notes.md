# Web scraping steps
1. Send a request to the url
2. Get all the HTML code from the page
3. Find the unique attribute (in the HTML code) of what you want - Eg: If you want all images on the page find its unique class, id, tag, etc.

# Url to crawl
- https://www.gumtree.com.au/s-clothing-jewellery/sneakers/k0c18308

# Useful links
- 403 error: https://stackoverflow.com/questions/38489386/python-requests-403-forbidden 
- Web crawler tutorial (freeCodeCamp): https://www.youtube.com/watch?v=SqvVm3QiQVk&t=824s
- Extract plain text from a HTML object: https://www.kite.com/python/answers/how-to-extract-text-from-an-html-file-in-python
- What .text does: https://www.codegrepper.com/code-examples/python/.text+in+python

# Notes - Descending order
080122: Found new url to crawl. Updating code in new file. Unsure if I will put url in README or modify code to allow user to input url. Input url might be a future feature.
080122: Created new webcrawler file - v2. archived v1. Next step: find new site to crawl.
080122: Finished steps 1 and 2 from below. printed url that it's trying to access, which is: https://www.bunnings.com.au/search/products?q=venetian%20blinds&sort=BoostOrder&page=1 - I follow the link and I can access the site. However, requests.get cannot access it. I get 403 error. Will now find another site to crawl to release MVP.
080122: Next steps:
    1.Get new git token - DONE
    2.Follow advice below - note from 051221 - DONE
    3.Find different site to crawl to release an MVP - DONE
051221: Got this advice (re:403 error) from Amigos code fb group: "Have it print the exact URL it's trying to access and see what happens when you paste that URL into a web browser." - Will try this. Group says might be issues relating to logging in.
281121: Coded out all the code from video 2. Return to resolving 403 error.
281121: .text is a method that converts HTML code to text. When you use the output from the .text conversion in a Beautiful soup object, the output for both appears to be the same. 
Ie: Two lines of code from the webcrawler:
    a.plain_text = source_code.text
    b.soup = BeautifulSoup(plain_text, "html.parser")
If you print the output of both these files its the same.
However, based on info at 0:50 in video 2, the point of line (b) is to:
    - convert to a BeautifulSoup object, and
    - convert the data to a format that BeautifulSoup can use to crawl through it, sift through it and sort through it.

281121: Before I try to fix 403 error I will try to work out how to get just the text from a website. I want to see how that works to understand it better. Refer to file
251121: Trying to fix 403 error when making site request. Line 11 - request.get() returns error.