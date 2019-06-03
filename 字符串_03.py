"""
split()分隔字符串，其中运行有一个参数，用来指定字符串
以什么字符分隔（默认为''），返回一个列表
"""
s = 'We all love Python'
print(s.split())

x = 'shiyanlou:is:waiting'
print(x.split(':'))

# join()使用指定的字符连接多个字符串
print('@'.join("GNU/Linux is great".split()))

# 字符串剥离
# strip(chars)用来剥离字符串中指定的字符。不指定参数默认剥离首尾的空格和换行符
s = ' a bc\n'
print(s.strip())

# lstrip()或rstrip()只对字符串左或右剥离
s = 'www.foss.in'
print(s.lstrip('cwsd.')) # 删除左边出现的'c','w','s','d','.'字符
print(s.rstrip('cnwdi,.'))