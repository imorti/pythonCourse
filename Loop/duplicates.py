numbers = [2, 2, 4, 5, 3, 4, 6]
uniques = []

# remove duplicates and add to uniques
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)