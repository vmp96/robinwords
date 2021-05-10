import random

class Node:
    def __init__(self, key, parent):
        self.key = key
        self.descendants = 0
        self.children = [None] * 26
        self.parent = parent

def generateTree(dictionary):
    root = Node("", None)

    #traverse down tree, create new nodes if "word path" doesn't exist yet
    for word in dictionary:
        curr = root
        for i in range(4):
            curr.descendants += 1 
            childIndex = ord(word[i])-97 
            if curr.children[childIndex] == None:
                curr.children[childIndex] = Node(word[i], curr)
            curr = curr.children[childIndex]    
        #at leaf
        curr.descendants = 1
    return root

#generate global tree

wordList = None
with open('four_letter_words.txt', 'r') as f:
    wordList = f.read().splitlines()
#Use this list to test endgame:
#wordList = ["home", "some","same", "tome", "tame", "game"]
#print(len(wordList))
tree = generateTree(wordList)

#returns set of numbers from 0 to size-1 in random order. Used for computer game option in getNeighbor and neighborSearch
def randOrder(size):
    numbersToPick = [*range(size)]
    order = []
    for i in range(size):
        pick = random.randint(0,size-1-i)
        order.append(numbersToPick[pick])
        numbersToPick = numbersToPick[0:pick]+numbersToPick[pick+1:size]
    return order

#returns word that is still in list that is neighbors with input word
def neighborSearch(word, wildcard, isRandom = False):
    wildcardParent = tree
    for i in range(wildcard):
        childIndex = ord(word[i])-97 
        if wildcardParent.children[childIndex] == None:
            return None
        wildcardParent = wildcardParent.children[childIndex]
    #fixed on wildcardParent. Check each child [a-z] for potential neighbor
    order = [*range(26)]
    if isRandom:
        order = randOrder(26)
    for i in order:
        curr = wildcardParent.children[i]
        #skip words not in tree and word matching input
        if curr == None or curr.key == word[wildcard] or curr.descendants==0:
            continue
        neighbor = word[:wildcard] + curr.key
        for j in range(1, 4-wildcard):
            childIndex = ord(word[wildcard+j]) - 97
            if curr.children[childIndex] == None:
                continue
            curr = curr.children[childIndex]
            neighbor+=curr.key

        if len(neighbor) == 4 and curr.descendants != 0:
            return neighbor
    
    return None

#Default: returns the first neighbor that neighborSearch finds. In a computer game: picks arbitrary letters as wildcard first. 
def getNeighbor(word, isRandom = False):
    letterOrder = [0,1,2,3]
    if isRandom:
        letterOrder = randOrder(4)
    for i in range(4):
        neighbor = neighborSearch(word, letterOrder[i], isRandom)
        if neighbor != None:
            return neighbor
    return None

def hasNeighbor(word):
    neighbor = getNeighbor(word)
    if neighbor == None:
        return False
    return True

#returns leaf node (last letter) of word if it is in the tree
def search(word):
    curr = tree
    for i in range(4):
        childIndex = ord(word[i]) - 97
        if curr.children[childIndex] == None:
            return None
        curr = curr.children[childIndex]
    return curr

#eliminates word from tree by reducing the descendants value from nodes
#does not delete nodes
def removeWord(word):
    leaf = search(word)
    if leaf == None:
       return False
    curr = leaf
    for i in range(4):
        curr.descendants -= 1
        curr = curr.parent
    return True

#string operation on words
def wordsAreNeighbors(x, y):
    differences = 0
    for i in range(4):
        if x[i] != y[i]:
            differences += 1
    if differences == 1:
        return True
    return False

def printTree(node):
    if node == None:
        return
    for children in node.children:
        if children != None:
            print(children.key, end=", ")
    print("")
    for children in node.children:
        printTree(children)

#Game Start
players = ["player","CPU"]
currentWord = ""
currentPlayer = 1

def swapTurn():
    global currentPlayer
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0

def checkMove():
    err = ""
    while err != "No Error!":
        wordAttempt = input(players[currentPlayer]+":").lower()
        #check if word is real 4 letter word
        wordNode = None
        if wordAttempt == "":
            global currentWord
            err = f"Last Word: {currentWord}"
        elif len(wordAttempt) != 4:
            err = "Must be a real four letter word."
        elif not wordAttempt.isalpha():
            err = "Must be a real four letter word of made up of letters [a-z]."
        else:
            wordNode = search(wordAttempt)
            if wordNode == None:
                err = "Must be a real four letter word."
            #check if word was used
            elif wordNode.descendants == 0:
                err = "That word has already been used."
            #check if neighbors
            elif not wordsAreNeighbors(currentWord,wordAttempt):
                err = "You can only change one letter at a time."
        
        if err != "":
            print(err)
            err = ""
        else:
            err = "No Error!"
    return wordAttempt


def nextTurn():
    swapTurn()
    wordGiven = checkMove()
    #wordGiven is a legal move
    #check for victory condition
    if(not hasNeighbor(wordGiven)):
        return True   
    #remove word from tree
    removeWord(wordGiven)
    global currentWord
    currentWord = wordGiven
    return False

def computerTurn():
    swapTurn()
    global currentWord
    wordGiven = getNeighbor(currentWord, True)
    print(f"CPU:{wordGiven}")
    if(not hasNeighbor(wordGiven)):
        return True   
    #remove word from tree
    removeWord(wordGiven)
    currentWord = wordGiven
    return False


def humanTurn():
    swapTurn()
    wordGiven = checkMove()
    #wordGiven is a legal move
    #check for victory condition
    if(not hasNeighbor(wordGiven)):
        return True   
    #remove word from tree
    removeWord(wordGiven)
    global currentWord
    currentWord = wordGiven
    return computerTurn()

def start2p():
    temp = input("Player 1 Name:")
    while(len(temp)>16 or temp == ""):
        if temp == "":
            temp = input("Please enter a name for player 1:")
        else:
            temp = input("Please try a shorter name.")
    players[0] = temp
    temp = input("Player 2 Name:")
    while(len(temp)>16 or temp == ""):
        if temp == "":
            temp = input("Please enter a name for player 1:")
        else:
            temp = input("Please try a shorter name.")
    players[1] = temp
    #pick random word from list to start
    global currentWord
    currentWord = wordList[random.randint(0,len(wordList)-1)]
    while (not hasNeighbor(currentWord)):
        currentWord = wordList[random.randint(0,len(wordList)-1)]
    removeWord(currentWord)
    print(currentWord)
    isEnd = nextTurn()
    while not isEnd:
        isEnd = nextTurn()
    #nextTurn returns, game over
    print("There are no more words.")
    print(players[currentPlayer]+" wins!")

def start1p():
    temp = input("Player Name:")
    while(len(temp)>16 or temp == ""):
        if temp == "":
            temp = input("Please enter a player name:")
        else:
            temp = input("Please try a shorter name.")
    players[0] = temp
    #pick random word from list to start
    global currentWord
    currentWord = wordList[random.randint(0,len(wordList)-1)]
    while (not hasNeighbor(currentWord)):
        currentWord = wordList[random.randint(0,len(wordList)-1)]
    removeWord(currentWord)
    print(currentWord)
    isEnd = humanTurn()
    while not isEnd:
        isEnd = humanTurn()
    #nextTurn returns, game over
    print("There are no more words.")
    print(players[currentPlayer]+" wins!")

print("Robinwords. Please check readme for instructions.")
gameMode = input("Play against computer? (Y/N)").capitalize()
while(gameMode!="Y" and gameMode!="N"):
    gameMode = input("Play against computer? (Y/N)").capitalize()

if gameMode == "Y":
    start1p()
else:
    start2p()