# need this library to work with dates
import datetime

#Open file
f = open("seasons.dat", "r")

#Get the number of sets
intNum = int(f.readline())

# loop through the sets
for x in range(0, intNum):
    # get the total distance that needs to be travelled
    distance = int(f.readline())
    # get the startdate and convert it into a datetime object using strptime
    startdate = datetime.datetime.strptime(f.readline().strip(), "%B %d, %Y")

    # set dayOfYear and count forward
    dayOfYear = startdate

    # do a loop until the entire distance has been travelled.
    while distance >= 0:
        # if the month is April or earlier, remove 3 miles from the distance left.
        if dayOfYear.month <=4:
            distance -=3
        # else if the month is August or earlier, remove 5 miles from the distance left.
        elif dayOfYear.month <= 8:
            distance -=5
        # otherwise remove 1 mile
        else:
            distance -=1

        # if we're not at the end yet, then add another day and loop again.
        if distance >= 0:       
           dayOfYear +=datetime.timedelta(days=1)

    # print the day that the person finishes travelling.
    print(dayOfYear.strftime("%B %d, %Y"))



