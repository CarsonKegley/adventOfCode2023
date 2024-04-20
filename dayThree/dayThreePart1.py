
from unicodedata import numeric


def getInput(path):
    file = open(path,"r")
    content = file.read()
    contentList = content.split("\n")
    return contentList

def isSpecialChar(character):
    return  not character.isalnum() and character != "."

def checkSurroundingChar(data):
    returnValue = 0
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            
            #Check if index is in the top left boundry
            if i == 0 and j == 0 and data[i][j].isnumeric():
                if isSpecialChar(data[i][j+1])or isSpecialChar(data[i+1][j]) or isSpecialChar(data[i+1][j+1]):
                    returnValue = returnValue + int(data[i][j])
            
            #Check if character is in the top right boundry
            if i == 0 and j == len(data[j])-1 and data[i][j].isnumeric():
                if isSpecialChar(data[i][j-1])or isSpecialChar(data[i+1][j]) or isSpecialChar(data[i+1][j-1]):
                    returnValue = returnValue + int(data[i][j]) 

            #Check if character is on top boundry
            

    return returnValue


data = getInput("./testInput.txt")

list_data = [list(line) for line in data]

print(checkSurroundingChar(list_data))

print(isSpecialChar(data[1][3]))