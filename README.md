1:  This program will be given a word to translate to English, and a language to translate from. It will use en.wiktionary.org's sites.

E.g.: "translate chat French" should print 

"chien m (plural chiens, feminine chienne)

1. dog
2. cock, hammer (of a firearm)"

2:  The procedure for finding definitions will be as follows:
Look up the word
Find the right paragraph for the specified language
Find the definition entries
    
2.1: If no translations are found, the program should return that it did not find an entry for the word.
2.2: If no exact entries are found for the word, but suggestions are made, the program should iterate over the suggestions and see if it finds an entry with the specified language. If this fails, see 2.1.
