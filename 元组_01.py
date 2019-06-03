a = 'd','e','f'
print(a)

print(a[1])

for x in a:
    print(x,end = ' ')
print()

# 元组的拆封和赋值
a = divmod(15,2)
x,y = a
print(a)
print(x)
print(y)

# 属性：不可变类型
# a = (1,2,3,4)
# del a[0]