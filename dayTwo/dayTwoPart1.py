#!/usr/bin/python3
data = []
returnVal = 0
for x in open("input.txt"):
    x = x.replace("\n","")
    game, parts= x.split(":")
    gameNum = game.replace("Game ", "")
    partSpliting = parts.split(";") 
    reconstitute = ",".join(partSpliting)
    shikiken = reconstitute.split(",")
    drop=[]
    for i in shikiken:
        num, col = i.strip().split(" ")
        drop.append([int(num),col])
    valid = True 
    for v in drop:
        if v[1] == "red" and int(v[0]) >12:
            valid = False
        elif v[1] == "green" and int(v[0]) > 13:
            valid = False
        elif v[1] == "blue" and int(v[0]) > 14:
            valid = False

    print(drop)
    if valid:
        returnVal += int(gameNum)
print(returnVal)
