#Write a program using a while statement, that prints out the two-digit number
#such that when you square it, the resulting three-digit number has its rightmost
#two digits the same as the original two-digit number.  That is, for a number in the form AB:
#AB * AB = CAB, for some C.

tel = 10
x = False

while x == False:
    square = tel**2
    last_two =  square % 100
    if last_two == tel:
        print(tel)
        x = True
    tel += 1
