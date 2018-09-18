#Write a program using a while statement, that given the number n as input, prints the first n odd numbers starting from 1.
#For example if the input is
#4
#The output will be:
#1
#3
#5
#7


num = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below

counter= 0 
odd_number= 1
while counter < num:
    print(odd_number)
    odd_number = odd_number + 2
    counter = counter + 1 
