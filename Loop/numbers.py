numbers = [3,6,10,2,8,4]
#find greatest value
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)