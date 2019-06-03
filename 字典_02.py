# 遍历字典items()
data = {'kushal':'Fedora','kart_':'Debian','Jace':'Mac'}

for x,y in data.items():
    print("{} uses {}".format(x,y))

# dict.setdefault()
data = {}
data.setdefault("names",[]).append('Ruby')
print(data)
data.setdefault('name',[]).append('Python')
print(data)
data.setdefault("name",[]).append('C')
print(data)

# 遍历列表（或任何序列类型）的同时获得元素索引值
for i,j in enumerate(['a','b','c']):
    print(i,j)