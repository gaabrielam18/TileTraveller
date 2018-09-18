pyg = 'ay'
pyg2 = 'yay'
vowel = 'a e i o u y'
word = str(input("Enter a word: "))
stadur = 0


while True:
    if word == '.':
        break
    else:
        for index,letter in enumerate(word):
            if letter in vowel:
                stadur = index 
                break
        for index,letter in enumerate(word):
            if letter in vowel:
                word = word + pyg2
                print(word)
                break
            elif letter not in vowel:
                word = word[stadur:] + word[:stadur] + pyg
                print(word)
                break
        
    word = str(input("Enter a word: "))
