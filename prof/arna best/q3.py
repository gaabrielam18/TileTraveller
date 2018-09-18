value =int(input("Initial value: "))
step = int(input("Step: "))
sum = value
values = " "

while sum < 100: 
    value_str = str(value)
    values += value_str + " " 
    value = value + step   
    sum = sum + value
print(values)
print("Sum og series: ", sum)