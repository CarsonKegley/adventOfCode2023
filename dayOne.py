def getInput(path):
    file = open(path,"r")
    content = file.read()
    cleanContent = content[:-1]
    contentList = cleanContent.split("\n")
    return contentList
    

def partOne():

    calibrationValues = getInput("input.txt")
    decodedValues = []

    numberWords = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    } 

    #Grabbing numbers from strings
    for line in calibrationValues:
        numbersInLine = ""
        for character in line:
            if character.isnumeric():
                numbersInLine = numbersInLine + character
        if len(numbersInLine) >2:
            numbersInLine = numbersInLine[0] + numbersInLine[-1]
        elif len(numbersInLine) == 1:
            numbersInLine = numbersInLine[0] + numbersInLine[0]

        decodedValues.append(numbersInLine)
        print(line +":"+numbersInLine)
    
    
    totalCalibrationValue = 0 
    for value in decodedValues:
        totalCalibrationValue += int(value)
    print(totalCalibrationValue)

def main():
    numberWords = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
    }



    
if __name__== "__main__":
    main()
