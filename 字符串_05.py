# 回文检查
s = input("Please enter a string: ")
z = s[::-1] # 倒序
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")