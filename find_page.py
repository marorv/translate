from sys import stdin
import re

def url_of_page(data):
    url_base = 'https://en.wiktionary.org'
    url = data[data.index('href="') + 6 : data.index('" title')]
    
    print(url_base + url)

lines = []
for str in stdin:
    lines.append(str)

word = lines[-2].strip()
language = lines[-1].strip()

indicator = '<strong>There is a page named "<a href="/wiki/' + word + '" title="' + word + '">' + word + '</a>" on this wiki.</strong> See also the other search results found.</p>'

found = False

for element in lines:
    if indicator.strip() == element.strip():
        found = True
        url_of_page(element)
        break
if found == False:
    print("Did not find a page") 



