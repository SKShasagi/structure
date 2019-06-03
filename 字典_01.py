data = {'kushal':'Fedora','kart_':'Debian','Jace':'Mac'}
print(data)

print(data['kart_'])

# 创建新的键值
data['parthan'] = 'Ubuntu'
print(data)

# 使用del关键字删除任意指定的键值
del data['kushal']
print(data)

# 使用 in 关键字查询指定的键是否存在于字典中
print('ShiYanLou' in data)

# Tip:字典中的键必须是不可变类型

# dict()可以从包含键值对的元组创建字典
print(dict((('A','a'),('B','b'))))