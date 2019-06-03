# 创建空集合请使用set(),而不是{}
a = set()
b = {}
print(type(a))
print(type(b))

basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)       # 可以看到重复得元素被去除

print('orange' in basket)
print('crabgrass' in basket)

# 演示对两个单词中的字母进行集合操作
a = set("abracadabra")
b = set('alacazam')
print(a)        # a 去重后的字母
print(b)
print(a - b)    # a 有而 b 没有的字母
print(a | b)    # 存在于a 或 b 的字母
print(a & b)    # a 和 b都有的字母
print(a ^ b)    # 存在于 a 或 b 但不同时存在的字母

# 在集合中添加或弹出元素
a = {'a','e','h','g'}
print(a.pop())
a.add('c')
print(a)
