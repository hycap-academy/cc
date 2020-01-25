# open file
f = open("stacker.dat", "r")

#Get the number of sets
intNum = int(f.readline())

# Loop through the sets
for n in range(0, intNum):
    rows,cols = f.readline().split()
    map1=[]
    for y in range(0, int(rows)):
        map1.append(f.readline().strip())

    blocks = [int(i) for i in f.readline().split()] 
    
    stacks1=[]
    for y in range(int(rows)-1, -1, -1):
        if y == int(rows)-1:
            for x in range(0, len(map1[y])):
                if map1[y][x]=="#":
                    stacks1.append(x)
    
    print(stacks1)