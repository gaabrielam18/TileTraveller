#Write a program that reads in 3 integers
#and prints out the maximum of the three.

num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

# Fill in the missing code below
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
elif (num3 >= num1) and (num3 >= num2):
    largest = num3

max_int = largest
print("The maximum is: ", max_int) # Do not change this line
