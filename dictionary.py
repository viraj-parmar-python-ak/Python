# Memory Maping in Dictonary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change
print("id of x:", id(x))
print("id of year:", id(x['year']))

# car["color"] = "red"
car["year"] = 1969

print(x) #after the change
print("id of x:", id(x))
print("id of year:", id(x['year']))


# print(car) #before the change
# print("id of car:", id(car))
# print("id of year:", id(car['year']))

# # car["color"] = "red"
# car["year"] = 1969

# print(car) #after the change
# print("id of car:", id(car))
# print("id of year:", id(car['year']))


# x = car.keys()

# print(x) #before the change
# print("id of x:", id(x))
# print("id of year:", id(x[2]))

# car["year"] = 1969
# car["color"] = "red"

# print(x) #after the change
# print("id of x:", id(x))
# print("id of year:", id(x[2]))