#Open file
f = open("presidents.dat", "r")

#Get the number of entries
strNum = f.readline()
intNum = int(strNum)

# loop through the entries
for x in range(0, intNum):
    # read each line and split it up into an array.
    bills=f.readline().split()

    # set a variable called total
    total = 0

    # go through the bills array and assign each item in bills to a variable called bill
    for bill in bills:
        # check what bill is, then add the appropriate value to total
        if bill=="Franklin":
            total+=100
        elif bill=="Grant":
            total+=50
        elif bill=="Jackson":
            total += 20
        elif bill=="Hamilton":
            total+=10
        elif bill=="Lincoln":
            total+=5
        elif bill=="Washington":
            total+=1

    # print the total
    print("$" + str(total))
