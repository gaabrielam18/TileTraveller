#A prime number is a whole number greater than 1 whose only factors are 1 and itself.
#Write a program using a while statement,
#that given an int as the input, prints out
#"Prime" if the int is a prime number, otherwise it prints "!Prime".


n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
prime = True 
# Do not changes the lines below
teljari = 2
while n > teljari:
    if n % teljari == 0:
        prime = False
    teljari = teljari + 1 
if prime:
    print("Prime")
else:
    print("!Prime")
