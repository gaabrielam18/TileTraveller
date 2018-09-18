import string
e = str(input("Enter a sentence: "))
digit = 0
upper = 0 
lower = 0
counter = 0

punctuation = string.punctuation

for index, letter in enumerate(e):
    if letter.isdigit() == True:
        digit = digit + 1
    elif letter.isupper() == True:
        upper = upper + 1 
    elif letter.islower() == True:
        lower = lower + 1
    elif letter in punctuation:
        counter = counter + 1 

print("{:>15}{:>5}".format("Upper case", upper))
print("{:>15}{:>5}".format("Lower case", lower))
print("{:>15}{:>5}".format("Digits", digit))
print("{:>15}{:>5}".format("Punctuation", counter))

