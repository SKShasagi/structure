# 同时遍历两个序列类型，zip()
a = ['R','r']
b = ['F','f']
for x,y in zip(a,b):
    print('{} uses {}'.format(x,y))