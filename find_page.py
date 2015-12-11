from sys import stdin
import re

lines = []
for str in stdin:
    lines.append(str)

word = lines[-2].strip()
language = lines[-1].strip()

print(word, language)

indicator = '<strong>There is a page named "<a href="/wiki/' + word + '" title="' + word + '">' + word + '</a>" on this wiki.</strong> See also the other search results found.</p>'

found = False

for element in lines:
    if indicator.strip() == element.strip():
        found = True
        print("Found a page")
        break
if found == False:
    print("Did not find a page") 



