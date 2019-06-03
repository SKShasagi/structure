import sys
x = int(input("请输入星号个数："))
if x == 0:
 exit()

else:
 
 while x >= 1:
  print('*' * x)
  x -= 1
