# open file
f = open("greedy.dat", "r")

#Get the number of sets
intNum = int(f.readline())

# loop through the sets
for x in range(0, intNum):

    # Get the number of cashiers and number of carts
    strNums = f.readline().strip().split()
    # the first number in the array is the number of cashiers
    cashiers = int(strNums[0])
    # the second number in the array is the number of carts
    carts = int(strNums[1])

    # read the next line which is the number of carts and how long they will take.
    # create a list called carts and assign all the cart durations to it.
    carts = f.readline().strip().split()

    # create an array (list) of cashiers
    cashier=[]

    # initialize each cashier as 0 (which means they are ready to take on a new cart)
    # if there are 3 cashiers, the loop will make 3 cashiers.
    for y in range(0, cashiers):
        cashier.append(0)

    # do the while loop while there are items left in the carts array.
    # each loop is one second.
    while len(carts) > 0:

        # loop through each of the cashiers.
        for n in range(0, cashiers):
            # if there are no more carts, then break out of the loop
            if len(carts)==0:
                break
            
            # if the cashier value is 0, then it is ready to take on a new cart
            if cashier[n]==0:
                # pop (remove) a cart from the cart array, and assign the number of seconds to the cashier.
                cashier[n] = int(carts.pop(0))
                # print the cashier number.  since the array is 0 based, we have to add 1.
                print(n+1)
            else:
                # if the cashier value is not 0, then subtract 1 second.  
                # keep subtracting 1 second every loop until it gets to 0, then we add a new cart.
                cashier[n]-=1

    # add a new line for each set of data.
    print()
            

