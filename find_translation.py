from sys import stdin
import re

lines = []
for str in stdin:
    lines.append(str)

word = lines[-2].strip()
language = lines[-1].strip()

language = language.title()

indic = '<h2><span class="mw-headline" id="French">French</span>'

found = False

for element in lines:
    if (re.match(r'<h2><span class="mw-headline" id="' + language + '">' + language + '</span>', element.strip())):
        print("Has an entry for " + word + " in " + language)
        found = True
        break

if found == False:
    print("Has an entry for " + word + ", but not in " + language)


