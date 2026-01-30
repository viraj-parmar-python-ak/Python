# Memory Maping in the String

# t = 'python'
# print(id(t))
# print("0: ",id(t[0]))
# print("1: ",id(t[1]))
# t = 'P' + t[1:]
# print("After changing the value in the string")
# print(id(t))
# print("0: ",id(t[0]))
# print("1: ",id(t[1]))


a = "this "
b = "string"

print("id of a:", id(a))
print("id of b:", id(b))

print("id of a[0]:", id(a[0]))
print("id of b[0]:", id(b[0]))

c = a + b
print(c)

print("id of c:", id(c))

print("id of a[0] in c:", id(c[0]))
print("id of b[0] in c:", id(c[5]))
