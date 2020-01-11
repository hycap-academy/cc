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


    # create a variable for the highest number ranking
    # start it at 0 for now.
    maxNum = 0
    #Loop through each of the friends
    for x in range(0, intNumOfFriends):
       
        #Read in the friend
        strLine = f.readline()
        strLine = strLine.strip()  #remove the \n at the end

        # split the string into friend and ranking
        AryFriend = strLine.split()

        # the 2nd item in the array AryFriend[1] is the ranking.  
        # convert it and store it in an int variable
        intIndex = int(AryFriend[1])

        
        # if the intIndex is more than maxNum, then reset maxNum to intIndex
        # we are trying to find the largest number ranking
        if intIndex > maxNum:
            maxNum = intIndex

        # store in the dictionary by ranking
        friends[str(intIndex)] = AryFriend[0]

    # create a string variable that will be printed in the end.
    friendsList=""

    # loop from the largest ranking number to 1.
    for y in range(maxNum, 0, -1):

        # check to see if the ranking (key) exists in the dictionary
        if str(y) in friends:
            #if so, then add the friend to the friendsList string variable
            friendsList += friends[str(y)] + ", "

    # Where you're all done, remove the last two characters ", "  then print
    print(friendsList[:-2])



    

