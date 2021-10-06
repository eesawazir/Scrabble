import sys
import random


TILES_USED = 0 # records how many tiles have been returned to user
SHUFFLE = False # records whether to shuffle the tiles or not

# inserts tiles into myTiles
def getTiles(myTiles):
    global TILES_USED
    while len(myTiles) < 7  and TILES_USED < len(Tiles):
        myTiles.append(Tiles[TILES_USED])
        TILES_USED += 1



# prints tiles and their scores
def printTiles(myTiles):
    tiles = ""
    scores = ""
    for letter in myTiles:
        tiles += letter + "  "
        thisScore = getScore(letter)
        if thisScore > 9:
            scores += str(thisScore) + " "
        else:
            scores += str(thisScore) + "  "

    print("\nTiles : " + tiles)
    print("Scores: " + scores)

# gets the score of a letter
def getScore(letter):
    for item in Scores:
        if item[0] == letter:
            return item[1]



scoresFile = open('scores.txt')
tilesFile = open('tiles.txt')

# read scores from scores.txt and insert in the list Scores
Scores = []
for line in scoresFile:
    line = line.split()
    letter = line[0]
    score = int(line[1])
    Scores.append([letter,score])
scoresFile.close()

# read tiles from tiles.txt and insert in the list Tiles
Tiles = []
for line in tilesFile:
    line= line.strip()
    Tiles.append(line)
tilesFile.close()

# decide whether to return random tiles
rand = input("Do you want to use random tiles (enter Y or N): ")
if rand == "Y":
    SHUFFLE = True
else:
    if rand != "N":
        print("You did not enter Y or N. Therefore, I am taking it as a Yes :P.")
        SHUFFLE = True
        
if SHUFFLE:
    random.shuffle(Tiles)


myTiles = []
getTiles(myTiles)
printTiles(myTiles)

########################################################################
# Write your code below this
########################################################################

# returns True if and only if target is in the collection (e.g., a string or a list)
def isIn(target, collection):
    for item in collection:
        if target == item:
            return True
    return False

# returns True if and only if word only contains English alphabets
def containsOnlyEnglishAlphabets(word):
    Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',  'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in word:
        if not isIn(letter.upper(),Alphabets):
            return False
    return True

# reads the data from a file and returns a list containing those items (\n removed)
def readFromFile(filename):
    aList = []
    file = open(filename)
    for line in file:
        line = line.strip()
        aList.append(line)
    file.close()
    return aList

# return True if and only if the word can be made using tiles in myTiles
def canBeMadeWithTiles(word, myTiles):
    # create a copy of the tiles as we do not want to change myTiles
    backupTiles = myTiles.copy()
    for letter in word:
        if not isIn(letter,backupTiles):
            return False
        else:
            backupTiles.remove(letter)
    return True

# return True if and only if it meets all three rules
def isValid(word,myTiles,dictionary):
    if not containsOnlyEnglishAlphabets(word):
        print("Only use English letters.")
        return False

    if not isIn(word,dictionary):
        print("I have never heard of this word.")
        return False

    if not canBeMadeWithTiles(word,myTiles):
        print("This word cannot be made using the tiles.")
        return False

    print("Cool this is a valid word")
    return True

# returns score of a word
def getWordScore(word):
    score = 0
    for letter in word:
        score += getScore(letter)
    return score

# returns best word and its score
def getBestWord(myTiles,dictionary):
    bestWord = ""
    bestScore = 0
    for word in dictionary:
        # word is valid only if it can be made using the tiles
        if canBeMadeWithTiles(word,myTiles):
            thisScore = getWordScore(word)
            # update the bestWord and its score if word is better than the current best word
            if thisScore > bestScore:
                bestWord = word
                bestScore = thisScore
            
    return bestWord,bestScore
            

# this function plays the game using the provided dictionary and provided tiles    
def playGame(dictionary,myTiles):

    inputWord = input("\nEnter a word: ")
    inputWord = inputWord.upper()
    while inputWord != "***" and not isValid(inputWord,myTiles,dictionary):
        inputWord = input("\nEnter a word: ")
        inputWord = inputWord.upper()

    if inputWord != "***":
        print("Score of this word is:",getWordScore(inputWord))
    else:
        print("Better luck next time!!!")
    
        
    bestWord, bestScore = getBestWord(myTiles,dictionary)
    if bestScore == 0:
        print("\nNo word can be made using these tiles")
    else:
        print("\nThe word",bestWord,"is the word with highest score. Its score is",bestScore)


dictionary  = readFromFile("dictionary.txt")
playGame(dictionary,myTiles)
