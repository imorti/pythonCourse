name = input("What is your name? ")
print('Hi ' + name)
birth_year = input("Birth year?: ")
age = 2020 - int(birth_year)
print("You are " + str(age))
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)