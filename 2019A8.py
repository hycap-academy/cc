# need the itertools library to use the combinations() function
import itertools

# open file
f = open("semiperfect.dat", "r")

#Get the number of sets
intNum = int(f.readline())

# Loop through the sets
for n in range(0, intNum):
    # read in the number we are evaluating
    intNum1 = int(f.readline())

    # create a list for divisors
    divisors = []

    # loop through from 1 to intNum1/2 to check for divisors
    for x in range(1, int(intNum1/2)+1):
        # if the remainder is 0, then it is a divisor
        if intNum1 % x==0:
            # add the divisor to the divisors list
            divisors.append(x)
        

    # check to see if the number is semiperfect
    # assume that it is not by setting the var semiPerfect = False
    semiPerfect = False

    # The sum could be any combination
    # Loop through from 1 to the number of divisors
    for y in range(1, len(divisors)+1):
        # aryCombo is a list of lists of all the possible combinations 
        # from the possible list of numbers [divisors] 
        # choosing y number of items.  
        aryCombo = itertools.combinations(divisors, y)
        
        # loop through each combination in aryCombo and check to see if the sum 
        # equals the original number intNum1
        for combo in aryCombo:
            # does the sum of the array combo equal intNum1?
            if sum(combo) == intNum1:
                # if it does, then set semiPerfect = True and exit out of the loop
                semiPerfect = True
                break

    # if semiPerfect is True then print SemiPerfect, otherwise print NOT Semiperfect.
    if semiPerfect:
        print("Semiperfect")
    else: 
        print("NOT Semiperfect")

