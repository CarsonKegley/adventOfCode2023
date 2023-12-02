def getInput(path):
    file = open(path,"r")
    content = file.read()
    file.close()
    cleanContent = content[:-1]
    contentList = cleanContent.split("\n")
    return contentList

numberWords = {
    
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }

calibrationValues = getInput("testInput.txt")

numberValue=[]
for value in calibrationValues:
    indexOfNumber = {} 
    for word, num in numberWords.items():
        indexOfWord= value.find(word)
        if indexOfWord != -1:
            indexOfNumber[indexOfWord] = num 
    for i in range(len(value)):
        if value[i].isnumeric():
            indexOfNumber[i] = value[i]
    sortedIndexDict = sorted(indexOfNumber.items())
    if len(sortedIndexDict) == 1:
        numberValue.append(str(sortedIndexDict[0][1]) + str(sortedIndexDict[0][1]))
    else:
        numberValue.append(sortedIndexDict[0][1]+ sortedIndexDict[-1][1])

for i in range(len(calibrationValues)):
    print(calibrationValues[i] + ":" + numberValue[i])

totalCalibrationValue = 0 
for value in numberValue:
    totalCalibrationValue += int(value)
print(totalCalibrationValue)

