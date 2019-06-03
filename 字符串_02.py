s = 'shi yan lou'
# title()返回字符串的标题版本，即单词首字母大写，其余字母小写
print(s.title())

# upper()返回字符串全部大写版本，反之lower()范虎字符串全部小写版本
print(s.upper())
print(s.lower())

# swapcase返回大小写交换后的版本
s = 'I am A pRoGraMMer'
print(s.swapcase())

# isalnum() 检查所有字符是否只有字母和数字
s = 'jdwb 2323bjb'
print(s.isalnum()) # s 中包含空格，所以返回false

# isalpha() 检查字符串之中是否只有字母
s = 'abcd'
print(s.isalpha())

