A = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(A)
#
# B = [(x,y) for x in [1,2,3] for y in [3,1,4] if x == y]
# print(B)
#
# C = [(x,y) for x in [1,2,3] for y in [3,1,4] ]
# print(C)

# 等同于
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))
print(combs)

# 列表推导式的嵌套
a = [1,2,3]
z = [x + 1 for x in [x**2 for x in a]]
print(z)