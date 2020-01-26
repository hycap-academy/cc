#Open file
f = open("poker.dat", "r")

#Get the number of sets
intNum = int(f.readline().strip())

# loop through the sets
for x in range(0, intNum):
    # create a dictionary of cards that are in the hand.  The key is cardvalue.  (e.g. A, 2, 3, 4, etc)
    # The value is the number of those cards we are holding
    dictCard = {}

    # cards is an array of cards we are holding.  We strip then split after reading from the file.
    cards = f.readline().strip().split()

    # loop through each card in the card array.
    for card in cards:

        # if the cardvalue is in dictCard already, then increment the value by 1
        # Otherwise, create a new entry for the card value and set it to 1 
        if card[0] in dictCard:
            dictCard[card[0]] +=1
        else:
            dictCard[card[0]] = 1
    
    # set a variable to track the highest value in the dictionary
    maxStrength = 0
    # loop through the dictionary
    for key, value in dictCard.items():
        # if the value of the dictionary is higher than what is held
        # in maxStrength, then assign value to maxStrength
        if value > maxStrength:
            maxStrength = value
    
    # print the highest strength number
    print(maxStrength)