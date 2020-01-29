customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

# access key
# print(customer["name"])

# access key that doesn't exist, but add default value
# print(customer.get("birthdate", "Jan 1 1980"))

# reset key value
# customer["name"] = "Jack Smith"
# print(customer["name"])

# add key value to dictionary
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])