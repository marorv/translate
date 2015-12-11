#!/bin/sh

word=$1
language=$2

if [ ! -z "$1" ] && [ ! -z "$2" ]; then

echo "Translate $1 from $2 to English"

curl "https://en.wiktionary.org/w/index.php?title=Special%3ASearch&profile=default&search=$word&fulltext=Search" > wiktionary-search.txt

echo "$word" >> wiktionary-search.txt
echo "$language" >> wiktionary-search.txt

python3.4 find_page.py < wiktionary-search.txt



else

echo "Lacking variables. Please specify a word and a language."

fi
