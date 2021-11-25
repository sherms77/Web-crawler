# wiki search based on user entering a subject
# testing to see if a link can be generated without requests or bs4 modules

subject = input ('Enter a Wikepdia subject: ')
wiki = 'https://en.wikipedia.org/wiki/' + subject # builds link to subject

print(wiki) # prints link
# outputs hyperlink in vs code
# does not appear as hyperlink in Python IDLE

