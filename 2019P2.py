#Open file
f = open("friends.dat", "r")

friends = {}

#Get the number of sets of friends
strNum = f.readline()
intNum = int(strNum)

#Loop through the sets of friends
for i in range(0, intNum):

    #Find the number of friends to read in
    strNumOfFriends = f.readline()
    intNumOfFriends = int(strNumOfFriends)

    maxNum = 0
    #Loop through each of the friends
    for x in range(0, intNumOfFriends):
       
        #Read in the friend
        strLine = f.readline()
        strLine = strLine.strip()  #remove the \n at the end

        AryFriend = strLine.split()

        intIndex = int(AryFriend[1])

        if intIndex > maxNum:
            maxNum = intIndex

        friends[str(intIndex)] = AryFriend[0]

    friendsList=""
    for y in range(maxNum, 0, -1):
        try:
            friendsList += friends[str(y)] + ", "
        except KeyError:
            doNothing=True
    

    print(friendsList[:-2])



    

