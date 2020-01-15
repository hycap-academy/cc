# imporat the math library so we can round up using .ceil()
import math

#Open file
f = open("time.dat", "r")

#Get the number of sets
intNum = int(f.readline())

# loop through the sets
for x in range(0, intNum):
    # get the num of data points and the multiplier
    data1 = f.readline().strip().split()
    numOfDat = int(data1[0])  # in python this isn't necessary, but we'll assign it to numOfDat anyway
    multiplier = int(data1[1])  # the highest number is supposed to be multiplied by the multiplier

    # one liner way of converting string into array of ints
    # intdataset = [int(n) for n in f.readline().strip().split()]
    # intdataset = list(map(int, f.readline().strip().split()))
    # The following 5 lines could be replaced by one the lines above.
    ##############
    strdataset = f.readline().strip().split()

    intdataset = []
    for data in strdataset:
        intdataset.append(int(data))
    ###############

    # get the maximum time from the intdataset array
    maxTime = max(intdataset)

    # the limit is supposed to be the maximum time multiplied by the multiplier
    # We divide by 1000 because the units are in ms and the answer needs to be in seconds.
    limit = maxTime * multiplier/1000

    # round up using math.ceil()
    print(math.ceil(limit))

