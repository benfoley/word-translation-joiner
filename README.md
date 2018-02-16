# word-translation-joiner
Create a wordlist from words and translations that have been separated into individual files.

```    
    .
    |---- languages
    |    |
    |    |---- marra
    |        |    
    |        |---- sounds
    |        |    |---- word1.wav
    |        |    |---- word2.wav
    |        |    
    |        |---- translations
    |        |    |---- word1.txt
    |        |    |---- word2.txt
    |        |    
    |        |---- words
    |             |---- word1.txt
    |             |---- word2.txt
    |
    |---- wordlist.py
```

Run it like:

    $ python3 wordlist.py -i languages/marra


Creates a `dict.txt` in the language folder.

```
guwarda ear
nyardin skin
marranguru  head
```