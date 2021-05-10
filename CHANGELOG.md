#### Features:
- Now there is an option to play against the computer. In the 1 player mode, the CPU will pick a random legal word from the list on its turn. 
- Attemping to pass an empty string as a word will no longer return an user error but will instead print the last accepted word. This is helpful when there have been multiple bad attempts and you need to know what the last word was.

#### Bug Fixes:
- Fixed bug that prevented endgame from triggering.
- Entering anything other than an alphabetic character caused a crash. Now there is an appropriate error message when trying to input these strings. 
- Control flow of user error messages changed so certain errors like the one above wouldn't default to "Must be a real four letter word." 

#### Other:
- nextTurn function that handled most of the game was recursive. That makes for poor memory use. Now the function returns true when the game ends and is ran in a loop. 

#### To Do:
- Get another list of words. This one has too many words that aren't in most dictionaries and is still missing others, notably plurals. 