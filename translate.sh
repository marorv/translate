#!/bin/sh

word=$1
language=$2

if [ ! -z "$1" ] && [ ! -z "$2" ]; then

echo "Translate $1 from $2 to English"

else

echo "Lacking variables. Please specify a word and a language."

fi
