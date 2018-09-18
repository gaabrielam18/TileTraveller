
def fun(num,txt):
    r = "r"
    l = "l"
    
    if 1<num<10:
    
        if txt == l:
            num -= 1 
            return num
        if txt == r:
            num += 1 
            return num
        else: 
            return num
    if num == 1:
        if txt == l: 
            return num
        if txt == r: 
            num += 1 
            return num
        else: 
            return num
    if num == 10:
        if txt == r: 
            return num
        if txt == l: 
            num -= 1 
            return num
        else: 
            return num

Position = int(input("Input a position between 1 and 10: "))
while True:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    move = input("Input your choice: ")
    out = fun(Position,move)
    if move == 'r':
        print("New position is: ", out)
        Position = out
    elif move == 'l':
        print("New position is: ", out)
        Position = out
    else: 
        Position = out
        print("New position is: ", out)
        
        break
    
    