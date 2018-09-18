#In golf, pars for a hole range from 3 to 5.  Write a program using a while statement that allows the user to input the par and the score for each of the 18 holes.  Based on the number of shots compared to par, the program writes out the following:
#"invalid score", for less than 3 under par
#"albatross", for 3 under par
#"eagle", for 2 under par
#"birdie", for 1 under par
#"bogey", for 1 over par
#"double bogey", for 2 over par
#"triple bogey", for 3 over par
#"bad hole", for scores more than 3 over par
#The input/output should look like this:
#Par of hole 1: 5
#Score on hole 1: 6
#bogey
#Par of hole 2: 4
#Score on hole 2: 4
#par
#Par of hole 3: 3
#Score on hole 3: 5
#double bogey
#Par of hole 4: 4
#Score on hole 4: 3
#birdie
#etc.

num_holes = 1

while num_holes <= 18:
    par = int(input("Par of hole " + str(num_holes)+": "))
    score = int(input("Score on hole " + str(num_holes) +": "))
    compared = par - score
    if 3 < compared:
        print("invalid score")
    elif 3 == compared:
        print("albatross")
    elif 2 == compared:
        print("eagle")
    elif 1 == compared:
        print("birdie")
    elif compared==0:
        print("par")
    elif -1 == compared:
        print("bogey") 
    elif -2== compared:
        print("double bogey")
    elif -3 == compared:
        print("triple bogey")
    elif -3 > compared: 
        print("bad hole")
    num_holes += 1
