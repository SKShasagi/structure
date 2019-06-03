"""
这是一个判断学生成绩是否打标的程序，要求输入学生数量，以及各个学生物理、
数学、历史三科的成绩，如果总成绩小于120，程序打印“fail”,否则打印“passed”
"""
n = int(input("Enter then number of students:"))
data = {} # 用来储存数据的字典变量
Subjects = ('Physics','Maths','History') # 科目
for i in range(0,n):
    name = input('Enter the name of the student{}'.format(i + 1)) # 获取学生名字
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of {}'.format(x)))) # 获取每门科目分数
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failed :(")
    else:
        print(x,"passed :)")
