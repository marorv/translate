from sys import stdin

lines = []
for str in stdin:
    lines.append(str)

indicator = '<strong>There is a page named "<a href="/wiki/chien" title="chien">chien</a>" on this wiki.</strong> See also the other search results found.</p>'

found = False

for element in lines:
    if indicator.strip() == element.strip():
        found = True
        print("Found a page")
        break
if found == False:
    print("Did not find a page") 
