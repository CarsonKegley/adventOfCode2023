data = []
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
    power = {"red":0,"green":0,"blue":0} 
    for n, v in drop:
        num = int(n)
        if v == "red" and num > power["red"]:
            power["red"] = num 
        if v == "green" and num > power["green"]: 
            power["green"] = num
        if v == "blue" and num > power["blue"]:
            power["blue"] = num
    result = power["red"] * power["green"] * power["blue"]
    data.append(result)

print(sum(data))