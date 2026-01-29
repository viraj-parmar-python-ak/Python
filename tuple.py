# x = ("apple", "banana", "cherry")
# print(hex(id(x)))
# print(hex(id(x[0])))
# print(hex(id(x[1])))
# y = list(x)
# print(hex(id(y)))
# y[1] = "kiwi"
# x = tuple(y)
# print(hex(id(x)))
# print(hex(id(x[0])))
# print(hex(id(x[1])))

# print(x)




# Add tuple to tuple
thistuple = ("apple", "banana", "cherry")
print(hex(id(thistuple)))
print(thistuple[0], hex(id(thistuple[0])))
print(thistuple[1], hex(id(thistuple[1])))
print(thistuple[2], hex(id(thistuple[2])))
y = ("orange",)
print(hex(id(y)))
thistuple += y
print(hex(id(thistuple)))

print(thistuple)


print(thistuple[0], hex(id(thistuple[0])))
print(thistuple[1], hex(id(thistuple[1])))
print(thistuple[2], hex(id(thistuple[2])))