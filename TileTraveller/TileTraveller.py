#Við ætlum að búa til breytu með staðsetningu 
#á meðan breytan er ekki 3,1 gefum við notendanum valmöguleika um 
#nýja staðsetningu
#sem sagt val notendans gefur honum nýja staðsteningu 
#leikurinn byrjar í 1,1

#travel = input("You can travel: ")
location = 11

while location is not 31:
    direction = 'd'
    #print("Direction: ", location)
    if location == 11: 
        print("You can travel: (N)orth.") 
        while direction not in 'n':
            direction = input("Direction: ").lower()
            if direction == 'n':
                location = 12
            else:
                print("Not a valid direction!")
    elif location == 12:
        print("You can travel: (N)orth or (E)ast or (S)outh.") 
        while direction not in 'nes':
            direction = input("Direction: ").lower()   
            if direction == 'n':
                location = 13
            elif direction == 'e':
                location = 22
            elif direction == 's':
                location = 11
            else:
                print("Not a valid direction!")
    elif location == 13:
        print("You can travel: (E)ast or (S)outh")
        while direction not in 'es': 
            direction = input("Direction: ").lower() 
            if direction == 'e':
                location = 23
            elif direction == 's':
                location = 12
            else:
                print("Not a valid direction!")
    elif location == 23:
        print("You can travel: (E)ast or (W)est.") 
        while direction not in 'ew':
            direction = input("Direction: ").lower() 
            if direction == 'e':
                location = 33
            elif direction == 'w':
                location = 13
            else:
                print("Not a valid direction!")
    elif location == 33:
        print("You can travel: (S)outh or (W)est.") 
        while direction not in 'sw':
            direction = input("Direction: ").lower() 
            if direction == 'w':
                location = 23
            elif direction == 's':
                location = 32
            else:
                print("Not a valid direction!")
    elif location == 32:
        print("You can travel: (N)orth or (S)outh.") 
        while direction not in 'ns':
            direction = input("Direction: ").lower() 
            if direction == 'n':
                location = 33
            elif direction == 's':
                location = 31
            else:
                print("Not a valid direction!")
    elif location == 22:
        print("You can travel: (S)outh or (W)est.")
        while direction not in 'sw': 
            direction = input("Direction: ").lower() 
            if direction == 'w':
                location = 12
            elif direction == 's':
                location = 21
            else:
                print("Not a valid direction!")
    elif location == 21:
        print("You can travel: (N)orth.") 
        while direction not in 'n':
            direction = input("Direction: ").lower()
            if direction == 'n':
                location = 22
            else:
                print("Not a valid direction!")

print("Victory!")





