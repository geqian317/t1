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
    name=input('请输入要增加的学生姓名:')
    list.append(name)
    return list

# 查询学生信息
def findStuednt(name):
    # x是索引,y是值
    for x, y in enumerate(list,1):
        if y == name:
            return x, y
    else:
        return -1,None

# 删除学生
def delStudent():
    name1=input('请输入要删除的学生姓名:')
    x, name = findStuednt(name1)
    if name1==name:
        list.remove(name1)
        return list
    else:
        print('T666班没有这个学员')

# 修改学生信息
def modifyStuednt():
    name=input('请输入要修改的学生姓名')
    name2=input('请输入修改后的学生姓名:')
    x,name=findStuednt(name)
    if x==-1:
        print('T666班没有这个学员')
    else:
        list[x]=name2
        return list

k=0
while k<=5:
    n=input('请输入你的选择:')
    if n=='0':
        student()
        print()
    elif n=='1':
        s=addStudent()
        print(s)
    elif n=='2':
        s=delStudent()
        print(s)
    elif n=='3':
        modifyStuednt()
    elif n=='4':
        name=input('请输入要查询的学生姓名:')
        x,y=findStuednt(name)
        print('{}在座位号{}的位置'.format(y, x))
        print('T666班没有这个学员')
    elif n=='exit':
        break
    else:
        print("输入错误,请重新输入")
    k+=1





