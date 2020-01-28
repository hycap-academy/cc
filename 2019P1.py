#Open file
f = open("clothes.dat", "r")

#Create 3 lists  (or stacks)
shirts = []
pants = []
socks = []

#Get the number of sets of clothes
strNum = f.readline()
intNum = int(strNum)

#Loop through the sets of clothes
for i in range(0, intNum):

    #Find the number of clothes items to read in
    strNumOfClothes = f.readline()
    intNumOfClothes = int(strNumOfClothes)

    #Loop through each of the clothes items
    for x in range(0, intNumOfClothes):

        #Read in the clothes item
        strLine = f.readline()
        strLine = strLine.strip()  #remove the \n at the end

        #Find where the "(" is
        idxSplit = strLine.find("(")

        #The text before the "(" is the item of clothes
        item = strLine[0:idxSplit-1]

        #The text after the "(" is the itemType (Shirt, Pants, Socks)
        itemType = strLine[idxSplit:]

        #Depending on what type of item it is, push it into the appropriate list.
        if itemType== "(shirt)":
            shirts.append(item)
        elif itemType=="(pants)":
            pants.append(item)
        elif itemType=="(socks)":
            socks.append(item)

    #Find the minimum number of items in the 3 lists.  
    #The instructions says that we should print out until clothes runs out
    #in one of the lists.
    numOfDays = len(shirts)
    if len(pants) < numOfDays:
        numOfDays = len(pants)
    
    if len(socks) < numOfDays:
        numOfDays = len(socks)

    #Loop through the minimum number of items in a list
    for y in range(0, numOfDays):
        #grab the last shirt, pants, and socks from each list. 
        MyShirt = shirts.pop()
        MyPants = pants.pop()
        MySocks = socks.pop()
        #print the shirt, pants, and socks
        print(MyShirt + ", " + MyPants + ", " + MySocks)
    
    #print a new line after each set of clothes.
    print()