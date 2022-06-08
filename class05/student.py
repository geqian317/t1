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

# 方法1
# print('-----------------------欢迎进入T666班学生管理系统-----------------------------')
# print('请选择系统功能：')
# print('0:显示所有学员信息')
# print('1:添加一个学员信息')
# print('2:删除一个学员信息')
# print('3:修改一个学员信息')
# print("4:查询一个学员信息")
# print("exit:退出学生管理系统")
#
# # 学员列表
# list = ['纪云禾', '长意', '洛洛', '林昊天', '雪三月']
# # 显示学员信息
# def student():
#     for i in list:
#         print(i,end='  ')
#
# # 添加学生
# def addStudent():
#     name=input('请输入要添加的学生姓名:')
#     list.append(name)
#     return list

# # 查询学生
# def findStuedent(name):
#     # x是下标,y是元素
#     for x,y in enumerate(list):
#         if y==name:
#             return x,y
#     else:
#         return -1,None

# # 删除学生
# def delStudent():
#     name1=input('请输入要删除的学生姓名:')
#     x,name=findStuedent(name1)
#     if name1==name:
#         list.remove(name1)
#         return list
#     else:
#         print("T666班不存在这个学生")

# # 修改学生
# def modifyStudent():
#     name=input('请输入要修改的学生姓名:')
#     name2=input('请输入修改后的学生姓名:')
#     x,name=findStuedent(name)
#     if x==-1:
#         print("T666班不存在这个学生")
#     else:
#         list[x]=name2
#         return list

# while True:
#     n=input('请输入你的选择:')
#     if n=='0':
#         student()
#         print()
#     elif n=='1':
#         l=addStudent()
#         print(l)
#     elif n=='2':
#         l=delStudent()
#         print(l)
#     elif n=='3':
#         l=modifyStudent()
#         print(l)
#     elif n=='4':
#         name=input('请输入要查询的学生姓名:')
#         x,y=findStuedent(name)
#         if x==-1:
#             print('T666班不存在这个学生')
#         else:
#             print('{}在座位号{}的位置'.format(y, x))
#     elif n=='exit':
#         print('退出系统')
#         break
#     else:
#         print('输入错误,请重新输入')

# 方法2
# 用列表存储班级,字典存储学员信息
Class_info=[]
# 界面使用函数
def print_ui():
    print('-------------欢迎进入T666班学生管理系统--------------')
    print('请选择系统功能：')
    print('0:显示所有学员信息')
    print('1:添加一个学员信息')
    print('2:删除一个学员信息')
    print('3:修改一个学员信息')
    print("4:查询一个学员信息")
    print("exit:退出学生管理系统")
    print("*"*50)
print_ui()

# 添加学员

def add_stu():
    new_id=input('请输入学员的编号:')
    new_name=input('请输入学员的姓名:')
    new_sex=input('请输入学员的性别:')
    # 姓名相同的提示,已存在 先循环所有人员,再判断
    for i in Class_info:
        if i['id']==new_id:
            print("此学员存在")
            # break退出 return不执行下面的代码
            return
    # 创建字典并将数据保存信息在字典中
    Student_info={}
    Student_info['id']=new_id
    Student_info['name']=new_name
    Student_info['sex']=new_sex
    # 将学生的信息存储在班级中
    Class_info.append(Student_info)
    print(Class_info)

# 删除学生信息
# 用户输入学员信息,学员存在就是删除,不存在提示不存在
def del_stu():
    del_name=input('请输入要删除的学生姓名:')
    for i in Class_info:
        if i['name']==del_name:
            Class_info.remove(i)
            break
    # else后面是整个循环结束才做的事情,因此和循环同级
    else:
        print('该学员不存在')
    print(Class_info)

# 修改学生信息
# 学员存在修改,学员不存在提示不存在
def update_stu():
    up_name=input("请输入要修改的学生姓名:")
    for i in Class_info:
        if i['name']==up_name:
            i['name']=input("请输入修改后学生姓名:")
            break
    else:
        print('该学员不存在')
    print(Class_info)

# 查询学员
def find_stu():
    find_name=input('请输入要查询的学生姓名:')
    for i in Class_info:
        if i['name']==find_name:
            print("学员信息:编号:{},姓名:{},性别:{}".format(i['id'],i['name'],i['sex']))
            break
    else:
        print('要查询学员不存在')
    print(Class_info)

# 显示学员信息
def dis_stu():
    for i in Class_info:
        print(i)

while True:
    print_ui()
    user_input=input('请输入你的选择:')
    if user_input=='0':
        dis_stu()
    elif user_input=='1':
        add_stu()
    elif user_input=='2':
        del_stu()
    elif user_input=='3':
        update_stu()
    elif user_input=='4':
        find_stu()
    elif user_input=='exit':
        print('退出系统')
        break
    else:
        print("输入错误,请重新输入")



print("---------欢迎进入T666班学生管理系统-----------")
print("请选择系统功能：")
print("0:显示所有学员信息：")
print("1:添加学员信息：")
print("2:删除学员信息：")
print("3:修改学员信息：")
print("4:查询学员信息：")
print("exit:退出学生管理系统")

# 界面
while True:
    chooes=input("请输入您的选择:")
if chooes == '0':
    dis_stu()
elif chooes == '1':
    add_stu()
elif chooes == '2':
    del_stu()
elif chooes == '3':
    update_stu()
elif chooes == '4':
    find_stu()
elif chooes == 'exit':
    print('您是否要退出系统?')
    n = input('yes退出,no不退出')
    if n == 'yes':
        break
else:
    print('输入有误,请重新输入')















# 4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
# def empty(str):
    # len(str)==0和str==''字符串为空,不包含空格
    # if len(str)==0:
    #     return True
    # else:
    #     return False
    # isspace()字符串只含空白字符(空格,"\t"、"\n"、"r"等),空字符串""不是空白字符。
    # if str.isspace()==True:
    #     return True
    # else:
    #     return False
    # str.strip()包含空格和为空
    # if not str.strip():
    #     return True
    # else:
    #     return False
# s=empty(input('请输入:'))
# print(s)





# 5.写函数，接收n个数字，求这些数字的和



# 6.定义一个函数,实现两个数四则运算,要注意有3个参数,分别是运算符和两个运算的数字.
# def operation(a,h,b):
#     str1=str(a)+h+str(b)
#     return eval(str1)
# print(operation(5,'+',1))
# print(operation(5,'-',1))
# print(operation(5,'*',1))
# print(operation(4,'/',1))








