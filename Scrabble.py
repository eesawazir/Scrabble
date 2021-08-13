import sys
import random

TILES_USED = 0  # records how many tiles have been returned to user
SHUFFLE = False  # records whether to shuffle the tiles or not


# inserts tiles into myTiles
def getTiles(myTiles):
    global TILES_USED
    while len(myTiles) < 7 and TILES_USED < len(Tiles):
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
    Scores.append([letter, score])
scoresFile.close()

# read tiles from tiles.txt and insert in the list Tiles
Tiles = []
for line in tilesFile:
    line = line.strip()
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
print()


# Check whether entered word is English
def check_if_english(word):
    check = word.isalpha()
    if check == False:
        return False


dic_lst = open("dictionary.txt").read().split()


# Search dictionary for entered word
def search(word, list):
    flag = True
    for i in range(len(list)):
        if list[i] == word:
            flag = True
            quit()
        else:
            flag = False

    if flag == False:
        return False


# Check whether tiles make up entered word
def check_tiles(word, myTiles):
    flag = True
    for letter in word:
        for j in range(len(myTiles)):
            if letter == myTiles[j]:
                flag = False

    if flag == False:
        return False
    else:
        return True


for i in range(100000):
    word_input = input("Enter a word: ").upper()
#
    if word_input == "***":
        print("Better luck next time!!!")
        quit()
    elif check_if_english(word_input) == False:
        print("Only use english letters!!!")
        print()

    elif search(word_input, dic_lst) == False:
        print("I have never heard of this word.")
        print()

    if check_tiles(word_input, myTiles) == False:
        print("This word cannot be made using your tiles.")
    else:
        print("Cool this is a valid word.")

# word_input = input("Enter a word: ").upper()
# check_tiles(word_input, myTiles)

