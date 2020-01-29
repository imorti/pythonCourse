numbers = [5, 2, 5, 2, 2]

# option 1
# for x_count in numbers:
#     print('x' * x_count)

#option 2
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

