f = open("clothes.dat", "r")

shirts = []
pants = []
socks = []


strNum = f.readline()
intNum = int(strNum)


for i in range(0, intNum):
    strNumOfClothes = f.readline()
    intNumOfClothes = int(strNumOfClothes)
    for x in range(0, intNumOfClothes):
        strLine = f.readline()
        strLine = strLine.strip()

        idxSplit = strLine.find("(")
        item = strLine[0:idxSplit-1]
        itemType = strLine[idxSplit:]

        if itemType== "(shirt)":
            shirts.append(item)
        elif itemType=="(pants)":
            pants.append(item)
        elif itemType=="(socks)":
            socks.append(item)

    numOfDays = len(shirts)
    if len(pants) < numOfDays:
        numOfDays = len(pants)
    
    if len(socks) < numOfDays:
        numOfDays = len(socks)

    for y in range(0, numOfDays):
        MyShirt = shirts.pop()
        MyPants = pants.pop()
        MySocks = socks.pop()
        print(MyShirt + ", " + MyPants + ", " + MySocks)
    
    print()