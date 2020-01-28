

def checkHorzBlocks(row1):
    HorzBlocks = []
    for i in range(0, len(row1)):
        if row1[i]=="#":
            HorzBlocks.append(i)
        else:
            if len(HorzBlocks) > 1:
                return HorzBlocks
            else:
                HorzBlocks.clear()
    return HorzBlocks

def checkVertBlocks(row1):
    VertStacks = []
    for i in range(0, len(row1)):
        if row1[i]=="#":
            if i==0:
                if row1[i+1]==".":
                    VertStacks.append(i)
            elif i < len(row1):
                if row1[i-1]=="." and row1[i+1]==".":
                    VertStacks.append(i)
            else:
                if row1[i-1]==".":
                    VertStacks.append(i)
    return VertStacks


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
    
    possible=True
    blocksUsed=0
    vertblocks = {}
    for y in range(int(rows)-1, -1, -1):
        horzBlocks =  checkHorzBlocks(map1[y]) 
        if len(horzBlocks) > 1:
            if len(horzBlocks) in blocks:
                blocks.remove(len(horzBlocks))
                blocksUsed+=1
                for m in range(0, len(horzBlocks)):
                    if horzBlocks[m] in vertblocks:
                        if vertblocks[str(m)] in blocks:
                            blocks.remove(vertblocks[str(m)])
                            vertblocks.pop(str(m))
                            blocksUsed+=1
                        else:
                            possible = False
                            break
            else:
                possible = False
                break

        aryVertBlocks = checkVertBlocks(map1[y])
        for j in range(0, len(map1[y])):
            if y < int(rows)-1:
                if j in aryVertBlocks and str(j) in vertblocks:
                    vertblocks[str(j)]+=1
                elif str(j) in vertblocks:
                    blocks.remove(vertblocks[str(j)])
                    vertblocks.pop(str(j))
                    blocksUsed+=1    
                elif j in aryVertBlocks:
                    vertblocks[str(j)]= 1
            else:
                if j in aryVertBlocks:
                    vertblocks[str(j)]= 1

                
                
    if possible:
        print(blocksUsed)
    else:
        print("Not Possible")
