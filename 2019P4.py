#Open file
f = open("population.dat", "r")

#Get the number of entries
strnum = f.readline()
intnum = int(strnum)

# loop through the entries
for x in range(0, intnum):
    # read each line and split it up into an array.
    data=f.readline().split()

    # set the initial population using the first item in the data array
    population=int(data[0])

    # count the number of seconds from 1 to specified number of seconds: data[1]
    # to do this, you have to use data[1] +1 because range will count up to 1 less than 
    # the second number.
    for n in range(1, int(data[1])+1):
        # using modulus - subtract 1 from population every 7 seconds
        if n % 7==0:
            population-=1
        # using modulus - add 1 from population every 4 seconds
        if n % 4==0:
            population+=1

    # print population
    print(population)

