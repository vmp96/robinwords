A copy of the game at https://robinwords.com/game/

### The Game:<br>
  Robinwords is a word game in which players take turns coming up with four letter words. Each word must share three letters with the word from the last turn. In other words, each new word must change one and only one letter from the last. Words cannot be reused. Players keep going back and forth until there is no possible word to come up with. The last player to enter a word wins. 


### create_word_list.py:<br>
  The legal word list was extracted from the nltk "words" corpus. The original list included names and proper nouns so the four letter words were crossreferenced with nltk "names" and matches were removed. Names that were also normal words like "dawn", "gene", and "rose" were manually excluded from this process. 


### robinwords.py:<br>
  The word list is used to generate a tree of height five. Each node can have 1 - 26 children and has a key which represents one letter in a word. This is made so traversal from root to leaf would spell out a single word. A node also stores the amount of its descendents.This structure is built in O(n) time. Because this program only deals in words of length 4, the tree allows for constant time access and removal. Crucially, it also allows for efficient search for "neighbor words" ie words that are one letter away from each other. This must be done every turn to determine end game. After this tree is generated, a two player game of Robinwords can begin.


### Future Improvements:<br>
  - Current word list contains words that don't exist in most dictionaries while missing a few other words. Notably, it seems to not have many plural words.

RobinWords was originally created by Jared Rhizor. This program was written for educational purposes only.
