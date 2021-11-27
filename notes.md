# Web scraping steps
1. Send a request to the url
2. Get all the HTML code from the page
3. Find the unique attribute (in the HTML code) of what you want - Eg: If you want all images on the page find its unique class, id, tag, etc.

# Useful links
- 403 error: https://stackoverflow.com/questions/38489386/python-requests-403-forbidden 
- Web crawler tutorial (freeCodeCamp): https://www.youtube.com/watch?v=SqvVm3QiQVk&t=824s
- Extract plain text from a HTML object: https://www.kite.com/python/answers/how-to-extract-text-from-an-html-file-in-python

# Notes - Descending order
281121: Before I try to fix 403 error I will try to work out how to get just the text from a website. I want to see how that works to understand it better. Refer to file
251121: Trying to fix 403 error when making site request. Line 11 - request.get() returns error.