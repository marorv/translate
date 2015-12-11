#!/bin/sh

word=$1
language=$2

word=$(echo $word | awk '{print tolower($0)}')

language=$(echo $language | awk '{print tolower($0)}')
language=$(echo $language | sed 's/.*/\u&/')

if [ ! -z "$1" ] && [ ! -z "$2" ]; then

echo "Translate $word from $language to English"

curl -s "https://en.wiktionary.org/w/index.php?title=Special%3ASearch&profile=default&search=$word&fulltext=Search" > wiktionary-search.txt

echo "$word" >> wiktionary-search.txt
echo "$language" >> wiktionary-search.txt

url_of_word=$(python3.4 find_page.py < wiktionary-search.txt)

curl -s $url_of_word > html-of-wiktionary-page.txt

echo "$word" >> html-of-wiktionary-page.txt
echo "$language" >> html-of-wiktionary-page.txt

python3.4 find_translation.py < html-of-wiktionary-page.txt



else

echo "Lacking variables. Please specify a word and a language."

fi
