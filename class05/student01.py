# 方法2
print('-----------------------欢迎进入T666班学生管理系统-----------------------------')
print('请选择系统功能：')
print('0:显示所有学员信息')
print('1:添加一个学员信息')
print('2:删除一个学员信息')
print('3:修改一个学员信息')
print("4:查询一个学员信息")
print("exit:退出学生管理系统")

stu_list=[]

def dis_stu():
    for i in stu_list:
        if len(stu_list)==0:
            print('暂无信息,请先添加')
        else:
            print(i)

def add_stu():
    new_id = input("请输入要添加的学生编号:")
    new_name=input("请输入要添加的学生姓名:")
    new_sex=input("请输入要添加的学生性别:")
    # 姓名相同的提示,已存在 先循环所有人员,再判断
    for i in stu_list:
        if i['id']==new_id:
            print("该学员已存在")
            # break是退出循环,return退出函数
            return
    # 创建字典保存学员信息
    stu_dict = {}
    stu_dict['id']=new_id
    stu_dict['name']=new_name
    stu_dict['sex']=new_sex
    # 将学生的信息添加到班级中
    stu_list.append(stu_dict)

def del_stu():
    del_name=input('请输入要删除的学生姓名:')
    for i in stu_list:
        if i['name']==del_name:
            stu_list.remove(i)
    else:
        print('该学生不存在')
    print(stu_list)

def update_stu():
    up_name=input("请输入要修改的学生姓名:")
    for i in stu_list:
        if i["name"]==up_name:
            i['name']=input('请输入修改后的学生姓名:')
    else:
        print('要修改的学生不存在')
    print(stu_list)

def find_stu():
    find_name=input("请输入要查询的学生姓名:")
    for i in stu_list:
        if i['name']==find_name:
            print('学员信息:编号:{},姓名:{},性别:{}'.format(i['id'],i['name'],i['sex']))
    else:
        print('要查询的学生不存在')

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
        n = input('yes退出,no不退出\n')
        if n == 'yes':
            break
    else:
        print('输入有误,请重新输入')
