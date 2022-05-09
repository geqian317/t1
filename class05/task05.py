# 1.写函数，接收两个数字参数，返回最大值
# 例如：
# 传入：10,20
# 返回：20
# def m(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# max=m(10,20)
# print(max)


# 2.写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
# 例如：
# 传入：[34,23,52,352,352,3523,5]
# 返回：[23,352,3523]
# list=[34,23,52,352,352,3523,5]
# # 写函数
# def odd(list):
#     # 创建新列表
#     list1=[]
#     # 循环遍历索引
#     for i in range(len(list)):
#         # 判断索引是否为奇数
#         if i%2!=0:
#             # list中索引为i的元素添加到新列表中
#            list1.append(list[i])
#     # 返回新列表
#     return list1
# li=odd(list)
# print(li)


# 3.写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
# 例如：
# 传入1：[34,23,52,352,666,3523,5]   	返回1：[34,23,52,352,666]
# 传入2：[34,23,52]     				返回2：[34,23,52]
# def list(list):
#     if len(list)>5:
#         return list[0:5]
#     else:
#         return list
# l=list([34,23,52,352,666,3523,5])
# l1=list([34,23,52])
# print(l)
# print(l1)


# 4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
# 例如：
# 传入："hello world"
# 返回：True
# def str(str1):
#     if str1.isspace():
#         return True
#     else:
#         return False
# s=str(input('请输入一个字符串'))
# print(s)


# 5.写函数，接收n个数字，求这些数字的和
# def sum1(*n):
#     sum=0
#     i=0
#     while i<=n:
#         sum=sum+i
#         i+=1
#     print(sum)
# s=sum1(1,2,3,4)
# print(s)


# 6.定义一个函数,实现两个数四则运算,要注意有3个参数,分别是运算符和两个运算的数字.
# 例如：
# 传入：10,*,20
# 返回：200


# 7.实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
# 要求1：使用一个list用于保存学生的姓名。
# 要求2：每一个功能定义一个自定义函数。界面如下：
# -----------------------欢迎进入T666班学生管理系统-----------------------------
# 请选择系统功能：
# 0:显示所有学员信息
# 1:添加一个学员信息
# 2:删除一个学员信息
# 3:修改一个学员信息
# 4:查询一个学员信息
# exit:退出学生管理系统
#
# (0)输入0后效果如下：
# 	0
# 	["郭易","汤碗珍"..]
#  (1)输入1后效果如下：
# 	1
# 	请输入增加人的姓名：张三
# 	["郭易","汤碗珍",'张三'..]
# (2)输入2后效果如下：
# 	2
# 	请输入删除人的姓名：张三
# 	["郭易","汤碗珍"..]
# (3)输入3后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	3
# 	请输入需要修改人的姓名：张三
# 	请输入需要修改后的姓名：李四
# 	["郭易","汤碗珍",'李四'..]
# (4)输入4后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	请输入查询人的姓名：张三
# 	郭易在座位号(3<下标>)的位置。
# (5)输入exit后效果如下：
# 	exit
# 	欢迎使用T666的学生管理系统，下次再见。


print('-----------------------欢迎进入T666班学生管理系统-----------------------------')
print('请选择系统功能：')
print('0:显示所有学员信息')
print('1:添加一个学员信息')
print('2:删除一个学员信息')
print('3:修改一个学员信息')
print("4:查询一个学员信息")
print("exit:退出学生管理系统")


# 学员列表
list = ['纪云禾', '长意', '洛洛', '林昊天', '雪三月']
# 显示学员信息
def student():
    for i in list:
        print(i,end=' ')
# 添加学生
def addStudent():
    name = input('请输入增加的学生姓名:')
    list.append(name)
    return list
#
def a():
    name=input("请输入要查询的学生姓名:")

# 查询学生
def findStuedent():
    name=a()
    # x是下标,y是元素
    for x, y in enumerate(list):
        if y==name:
            print('{}在座位号{}的位置'.format(y, x))
            return x, y
    else:
        print("T666班没有这个学员")

# 删除学生
def deletStudent():
    name1=input('请输入要删除的学生姓名')
    x,name=findStuedent(name1)
    if name1==name:
        list.remove(name1)
        return list
    else:
        print("T666班没有这个学员")


# 修改学生
def editStudent():
    name=input('请输入要修改的学生姓名')
    name1=input('请输入修改后的学生姓名')
    x,name=findStuedent(name)
    if x==-1:
        print("T666班没有这个学员")
    else:
        list[x]=name1
        return list

# 循环输入选择
i=0
while i<=5:
    n=input("请输入你的选择:")
    if n=='0':
        student()
        print()
    elif n=='1':
        s=addStudent()
        print(s)
    elif n=='2':
        s=deletStudent()
        print(s)
    elif n=='3':
        editStudent()
    elif n=='4':
        name=input()
        findStuedent(name)
    elif n=='exit':
         break
    else:
        print("输入错误,请重新输入")
        # continue
    i+=1






#         add()
#         print(list)
#     elif n == '2':
#         delect()
#         print(list)




# 求解鸡兔同笼问题,用户输入头和脚,然后程序输出鸡和兔的数量
# a=input("请输入头的数量:")
# b=input('请输入脚的数量:')
# def num(a,b):
#     # x+y=a
#     # 2x+4y=b
#     y=b/2-a
#     x=2a-b/2
