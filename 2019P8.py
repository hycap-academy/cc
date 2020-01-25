#Open file
f = open("poker.dat", "r")

#Get the number of sets
strNum = f.readline()
intNum = int(strNum)

# loop through the sets
for x in range(0, intNum):

    correct = int(f.readline())
 
    me=f.readline()
    friend = f.readline()

    incorrect = len(me) - correct

    maxCorrect = 0

    same = 0
    different = 0

    for i in range(0, len(me)):
        if me[i]==friend[i]:
            same +=1
        else:
            different +=1

    if same > correct:
        maxCorrect=correct
    else:
        maxCorrect=same

    if different > incorrect:
        maxCorrect+=incorrect
    else:
        maxCorrect += different

    print(maxCorrect)