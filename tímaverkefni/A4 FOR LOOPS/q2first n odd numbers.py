#Write a Python program using a for loop that, given the number n as input, prints the first n odd numbers starting from 1.
#For example if the input is:
#4
#The output will be:
#1
#3
#5
#7


num = int(input("Input an int: "))

odd_number = 1

for n in range(0, num):
    print(odd_number)
    odd_number = odd_number + 2
