#Write a program using a while statement, that given an int as the input, prints all the factors of that number, one in each line.
#For example, if the input is
#15
#The output will be
#1
#3
#5
#15

n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
teljari=1
while teljari <= n:
    if n % teljari == 0:
        print(teljari)
    teljari = teljari +1 
