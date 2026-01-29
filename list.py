lst = [i for i in range(10)]

sq = [val**2 for val in lst]
print(sq)

odd = [val for val in lst if val % 2 == 0]
print(odd)

c = [(x,y) for x in range(3) for y in range(3)]
print(c)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
li = [val for row in mat for val in row]
print(li)
