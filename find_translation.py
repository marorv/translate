#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin
import re

lines = []
for str in stdin:
    lines.append(str)

word = lines[-2].strip()
language = lines[-1].strip()

language = language.title()

indic = '<h2><span class="mw-headline" id="French">French</span>'

def find_defin(index, end):

    definitions = []
    clean_lines = []

    for j in range(index, end):
        if (re.match(r'<h4><span class="mw-headline" id=".*">.*</span><span class="mw-editsection"><span class="mw-editsection-bracket">.*', lines[j])):
            if lines[j + 2].strip() == '<ol>':
                i = j + 3
                while lines[i].strip() != '</ol>':
                    if re.match(r'<li>.*</li>', lines[i]):
                        definitions.append(lines[i])
                    i += 1 

    for element in definitions:
        clean_lines.append("")
    
    n=0
    for line in definitions:
        l = len(line.strip()) - 1
        for i in range(l):
            j = 1
            if line[i] == '>':
                while line[i + j] != '<':
                    clean_lines[n] += line[i + j]
                    j += 1
                    
        n += 1 

    print_result(clean_lines)
    
def print_result(results):
    for i in range(len(results)):
        print(i, end=""),
        print(':', results[i])

found = False
index = None

for element in lines:
    end_of_this_language = len(lines) - 1
    if (re.match(r'<h2><span class="mw-headline" id="' + language + '">' + language + '</span>.*', element.strip())):
        index = lines.index(element)
        print("Has an entry for " + word + " in " + language)
        found = True
    elif found == True and re.match(r'<h2><span class="mw-headline" id=".*">.*</span>.*', element.strip()):
        end_of_this_language = lines.index(element)        

        break

find_defin(index, end_of_this_language)
    

if found == False:
    print("Has an entry for " + word + ", but not in " + language)

