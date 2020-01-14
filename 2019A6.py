#Open file
f = open("rewordwrap.dat", "r")

#Get the number of sets
intNum = int(f.readline())

# loop through the sets
for x in range(0, intNum):
    # gets the max Chars per line and the number of lines
    maxChars = int(f.readline())
    lines = int(f.readline())

    # creates a list to store the words separately in an array
    words = []

    # loops through each line and stores all of the words in an array
    for n in range(0, lines):
        strLine = f.readline().strip()
        words.extend(strLine.split())  # .extend() adds an array to the existing "words" array.


    # creates a variable to count the number of characters in a line.
    length = 0

    # Loops through each word
    for word in words:
        # check to see if adding the next word will exceed the maximum number of characters (maxChars)
        if length + len(word) <= maxChars:
            # if the word will fit, then print the word and add the length of the word to length
            print(word, end=" ")
            length+=len(word)+1
        else:
            # if the word will not fit, print a new line, then print the wordpygame.examples.aliens.main()
            print()
            print(word, end=" ")
            # reset the length to the length of the word that was just printed.
            length=len(word)+1
            
    # create space between sets        
    print()
    print()
        