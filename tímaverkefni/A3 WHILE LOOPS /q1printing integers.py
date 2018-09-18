#Write a program using a while statement, that given an integer as input, prints all the integers starting from 1 up to but not including that number. Print one number per line.
#For example if the input is
#4
#the output should be:
#1
#2
#3


num = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below

counter = 1

while counter < num:
    print(counter)
    counter = counter + 1
