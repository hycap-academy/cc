f = open("population.dat", "r")

strnum = f.readline()
intnum = int(strnum)

for x in range(0, intnum):
    data=f.readline().split()
    population=int(data[0])

    for n in range(1, int(data[1])+1):
        if n % 7==0:
            population-=1
        if n % 4==0:
            population+=1

    print(population)

