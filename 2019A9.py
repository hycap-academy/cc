
# The purpose of this function is to check if another word can be formed with the remaining letters in the sentence.
# For instance if "i" and "in" are in the words array, then there would be a problem if the sentence was:
# thenowisnothing
# because it would recognize "i" as a word and leave snothing as the remainder of the sentence.  This function checks 
# to see if the next set of letters will also create a word in the words array.  If so, it'll return True.  Else false.

def findNextWord(sentence, words):
    # Create a word using the currentword variable by going to the remaining
    # letters in sentence by adding one letter at a time to currentword
    currentword=""

    #loop through each letter in sentence
    for y in range(0, len(sentence)):
        # Add one letter at a time from sentence to currentword
        currentword+=sentence[y]

        # if the next set of letters creates a word in the words array, then return True.
        if currentword in words:
            return True
    
    # If after going through the entire sentence, there is no match with a word from the words array
    # then return False
    return False

###   Start the main program    ###
# open file
f = open("spaces.dat", "r")

#Get the number of sets
intNum = int(f.readline())

words = []
# Loop through all of the words and put them into the words array
for n in range(0, intNum):
    words.append(f.readline().strip())  #strip is to remove the \n at the end of each line.

# read in the last line which is the full sentence.
sentence = f.readline().strip()

# cursor is the placeholder of where we are in the sentence.
cursor=0
# We will add a letter at a time to current word until it makes a word in the words array.
currentword=""

# iterate through each letter in sentence
for i in range(0, len(sentence)):
    # add each letter to currentword.
    currentword += sentence[i]

    # if currentword is in the array words, then check to see 
    # if we can create another word with the next set of letters
    if currentword in words:
        # findNextWord checks to see if another word can be created with the next set of letters
        if findNextWord(sentence[i+1:], words):
            # if there is a good match (and a word can be create with the next set of letters),
            # then reset currentword, increment the cursor by 1, and print the cursor position.
            currentword=""
            cursor+=1
            print(cursor, end=" ")

    # increment the cursor position by 1
    cursor+=1