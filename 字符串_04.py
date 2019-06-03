# 字符串搜索
s = 'faulty for a reason'
print(s.find('for'))
print(s.find('fora')) # 没有找到返回-1，找到返回索引
print(s.startswith("fa"))  # 检查以'fa'开头
print(s.endswith('reason')) # 检查以'reason' 结尾