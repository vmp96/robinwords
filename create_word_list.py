from nltk.corpus import words
from nltk.corpus import names

#get words
word_list = words.words()

#get four letter names 
fourLetterNames = {}
for name in names.words():
    if len(name) == 4:
        fourLetterNames.update({name.lower():""})
#remove regular words from name list
fourLetterNames.pop("bird")
fourLetterNames.pop("bill")
fourLetterNames.pop("bell")
fourLetterNames.pop("dale")
fourLetterNames.pop("dawn")
fourLetterNames.pop("dell")
fourLetterNames.pop("deny")
fourLetterNames.pop("doll")
fourLetterNames.pop("dove")
fourLetterNames.pop("else")
fourLetterNames.pop("faun")
fourLetterNames.pop("fawn")
fourLetterNames.pop("fern")
fourLetterNames.pop("gale")
fourLetterNames.pop("gene")
fourLetterNames.pop("gill")
fourLetterNames.pop("glad")
fourLetterNames.pop("gray")
fourLetterNames.pop("hope")
fourLetterNames.pop("iris")
fourLetterNames.pop("jade")
fourLetterNames.pop("jean")
fourLetterNames.pop("june")
fourLetterNames.pop("lamb")
fourLetterNames.pop("lane")
fourLetterNames.pop("love")
fourLetterNames.pop("lust")
fourLetterNames.pop("nova")
fourLetterNames.pop("opal")
fourLetterNames.pop("page")
fourLetterNames.pop("pier")
fourLetterNames.pop("rose")
fourLetterNames.pop("ruby")
fourLetterNames.pop("star")
fourLetterNames.pop("vale")
fourLetterNames.pop("wren")
fourLetterNames.pop("wynn")
fourLetterNames.pop("barn")
fourLetterNames.pop("bear")
fourLetterNames.pop("buck")
fourLetterNames.pop("burl")
fourLetterNames.pop("case")
fourLetterNames.pop("chip")
fourLetterNames.pop("clay")
fourLetterNames.pop("dean")
fourLetterNames.pop("hunt")
fourLetterNames.pop("park")
fourLetterNames.pop("puff")
fourLetterNames.pop("rabi")
fourLetterNames.pop("reed")
fourLetterNames.pop("rice")
fourLetterNames.pop("rich")
fourLetterNames.pop("rock")
fourLetterNames.pop("skip")
fourLetterNames.pop("slim")
fourLetterNames.pop("spud")
fourLetterNames.pop("stew")
fourLetterNames.pop("temp")
fourLetterNames.pop("tome")
fourLetterNames.pop("town")
fourLetterNames.pop("tray")
fourLetterNames.pop("trip")
fourLetterNames.pop("tuck")
fourLetterNames.pop("vail")
fourLetterNames.pop("wade")
fourLetterNames.pop("wait")
fourLetterNames.pop("wake")
fourLetterNames.pop("ward")
fourLetterNames.pop("ware")
fourLetterNames.pop("wash")
fourLetterNames.pop("west")
fourLetterNames.pop("will")
fourLetterNames.pop("wilt")
fourLetterNames.pop("wolf")
fourLetterNames.pop("wood")
fourLetterNames.pop("yank")
fourLetterNames.pop("yard")

print(fourLetterNames)

#subtract set of names from words/.
fourWords = []
for word in word_list:
        if len(word) == 4:
            if not (word.lower() in fourLetterNames):
                fourWords.append(word.lower()+"\n")

with open('four_letter_words.txt', 'w') as f:
    f.writelines(fourWords)

print("Created a file with "+str(len(fourWords))+" words.")