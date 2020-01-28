
def move(_beenthere, _map, _cp):
    x = _cp[0]
    y = _cp[1]
    _newbt = _beenthere.copy()
    _newbt.append((x, y))
    #print(_newbt)

    #print(_beenthere)
    mapwidth = len(_map[0])-1
    mapheight = len(_map)-1
    terrain = _map[y][x]
    days = 0
    if terrain == ".":
        days = 3
    elif terrain == "F":
        days = 5
    elif terrain == "W":
        days = 8
    elif terrain == "S":
        days = 0
    else:
        return -1

    possibledays = []

    if x == 1:
        return days
    else:

        # moveWest
        if (x-1, y) not in _beenthere and _map[y][x-1] != "R":
            #_cp[0] = x-1
            returnDays = move(_newbt, _map, [x-1, y])
            if returnDays > 0:
                possibledays.append(days + returnDays)

        # moveNorth
        if y > 0 and (x, y-1) not in _beenthere and _map[y-1][x] != "R":
            #_cp[1] = y-1
            returnDays = move(_newbt, _map, [x, y-1])
            if returnDays > 0:
                possibledays.append(days + returnDays)
        
        # moveSouth
        if y < mapheight and (x, y+1) not in _beenthere and _map[y+1][x] != "R":
            #_cp[1] = y+1
            returnDays = move(_newbt, _map, [x, y+1])
            if returnDays > 0:
                possibledays.append(days + returnDays)

        # moveEast
        if x < mapwidth and (x+1, y) not in _beenthere and _map[y][x+1] != "R":
            #_cp[0] = x+1
            returnDays = move(_newbt, _map, [x+1, y])
            if returnDays > 0:
                possibledays.append(days + returnDays)




        


    if len(possibledays) > 0:
        return min(possibledays)
    else:
        #print("dead end")
        return -1


        

# open file
f = open("trail.dat", "r")

#Get the number of sets
intNum = int(f.readline())


# Loop through each set
for n in range(0, intNum):
    rows,cols = f.readline().split()
    map1=[]
    currentpos = [0,0]
    beenthere = []
    for y in range(0, int(rows)):
        currentRow = f.readline().strip()
        map1.append(currentRow)
        if "S" in currentRow:
            currentpos[0] = currentRow.find("S")
            currentpos[1] = y

    deadline = int(f.readline().strip())
    
    days = move(beenthere, map1, currentpos)

    print(days)


