#学生管理系统
import os.path


def main():
    while True:
        menu()
        answer = int(input('请选择功能'))
        if answer in [0,1,2,3,4,5,6,7]:
            if answer==0:
                ans = input('确定退出系统吗？y/n')
                if ans == 'y' :
                    print('谢谢您的使用')
                    break
                else:
                    continue
            elif answer==1:
                insert()
            elif answer==2:
                search()
            elif answer==3:
                delete()
            elif answer==4:
                modify()
            elif answer==5:
                sort()
            elif answer==6:
                total()
            elif answer==7:
                show()
        else: print('请重新输入')

def menu():
    print('======================学生管理系统====================')
    print('-------------------------操作菜单---------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出系统')
    print('----------------------------------------------------')

def insert():
    student_list = []
    while True:
        try:
            id = int(input('请输入学生id（如1001）：'))
            name = input('请输入学生姓名：')
            english = int(input('请输入学生英语成绩：'))
            python = int(input('请输入学生python成绩：'))
            java = int(input('请输入学生java成绩：'))
        except:
            print('不合法，请重新输入')
            continue

        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        ans = input('是否继续录入学生信息？y/n')
        if ans == 'y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完成')

def save(student_list):
    try:
        file=open('students.txt','a',encoding='utf-8')
        for item in student_list:
            file.write(str(item)+'\n')
        file.close()
    except:
        file = open('students.txt', 'w',encoding='utf-8')
        for item in student_list:
            file.write(str(item) +'\n')
        file.close()

def search(): #按照姓名或者id号查找学生，并列出成绩
    flag = True
    while flag:
        answer = int(input('id查找请输入1，姓名查找输入2'))
        if answer == 1:
            while flag:
                try:
                    sea_id = int(input('输入要查找的学生id'))
                    with open('students.txt','r',encoding='utf-8') as file:
                        stu_old = file.readlines()
                        stu_id = []
                        for item in stu_old:
                            d = dict(eval(item))
                            stu_id.append(d['id'])
                        if (sea_id in stu_id):
                            for item in stu_old:
                                d = dict(eval(item))
                                if d['id'] == sea_id:
                                    print('id \t\t 姓名 \t 英语  Python  JAVA')
                                    print('{0} \t {1} \t {2} \t {3} \t {4}'.format(d['id'], d['name'], d['english'], d['python'],d['java']))
                        else:
                            print(f'找不到{sea_id}学生')
                except:
                    print('只能输入类1001型')
                ans = input('是否继续查找学生信息？y/n')
                if ans == 'y':
                    continue
                else:
                    flag=False
        elif answer == 2:
            while flag:
                sea_name = input('输入要查找的学生姓名')
                with open('students.txt', 'r', encoding='utf-8') as file:
                    stu_old = file.readlines()
                    stu_name = []
                    for item in stu_old:
                        d = dict(eval(item))
                        stu_name.append(d['name'])
                    if (sea_name in stu_name):
                        for item in stu_old:
                            d = dict(eval(item))
                            if d['name'] == sea_name:
                                print('id \t\t 姓名 \t 英语  Python  JAVA')
                                print('{0} \t {1} \t {2} \t {3} \t {4}'.format(d['id'], d['name'], d['english'],d['python'], d['java']))
                    else:
                        print(f'找不到{sea_name}学生')
                ans = input('是否继续查找学生信息？y/n')
                if ans == 'y':
                    continue
                else:
                    flag=False

        else:
            print('仅允许输入1或2')

def delete():
    while True:
        del_id = int(input('输入要删除的学生id'))
        if del_id != '':
            with open('students.txt','r',encoding='utf-8') as file:
                stu_old=file.readlines()
                stu_new=[]
                flag = False
                for item in stu_old:
                    d = dict(eval(item))
                    if d['id'] != del_id:
                        stu_new.append(d)
                    else:
                        flag=True
                if flag:
                    print(f'id为{del_id}的学生已删除')
                else:
                    print(f'无id为{del_id}的学生信息')
            with open('students.txt','w') as file:
                for item in stu_new:
                    file.write(str(item) + '\n')
                file.close()
        else:
            print('输入为空，请重新输入：')
            continue
        ans = input('是否继续删除学生信息？y/n')
        if ans == 'y':
            continue
        else:
            break
    print('已删除')
    show()

def modify():
    while True:
        mod_id = int(input('输入要修改的学生id'))
        with open('students.txt','r',encoding='utf-8') as file:
            stu_old=file.readlines()
            stu_new = []
            stu_id = []              #判断输入的值是否存在
            for item in stu_old:
                d = dict(eval(item))
                stu_id.append(d['id'])
            if (mod_id in stu_id):
                print(f'找到了{mod_id}学生')
            else:
                print(f'找不到{mod_id}学生')
                ans = input('是否继续修改学生信息？y/n')
                if ans == 'y':
                    continue
                else:
                    break
            for item in stu_old:  #修改学生信息
                d = dict(eval(item))
                if d['id'] == mod_id:
                    name = input('请输入学生姓名：')
                    english = int(input('请输入学生英语成绩：'))
                    python = int(input('请输入学生python成绩：'))
                    java = int(input('请输入学生java成绩：'))
                    stu_new.append(dict(id=mod_id,name=name,english=english,python=python,java=java))
                else:
                    stu_new.append(d)
        with open('students.txt', 'w',encoding='utf-8') as file:
            for item in stu_new:
                file.write(str(item) + '\n')
        ans = input('是否继续修改学生信息？y/n')
        if ans == 'y':
            continue
        else:
            break

def sort():
    show()
    if os.path.exists("students.txt"): #判断文件是否存在
        with open('students.txt','r',encoding='utf-8') as file:
            sort_list=file.readlines()
        sort_stu=[]
        for item in sort_list:
            d = dict(eval(item))
            sort_stu.append(d)
        answer = input("升序排列输入1，降序排列输入2")
        if answer=='1':
            sort_stu_bool = False
        elif answer =='2':
            sort_stu_bool = True
        else:
            print('非法字符，重新输入')
        answer = input("英语排序输入1，Python排序输入2，Java排序输入3，总分排序输入4")
        if answer=='1':
            sort_stu.sort(key=lambda x:int(x['english']),reverse=sort_stu_bool)
            show_students(sort_stu)
        elif answer =='2':
            sort_stu.sort(key=lambda x:int(x['python']), reverse=sort_stu_bool)
            show_students(sort_stu)
        elif answer =='3':
            sort_stu.sort(key=lambda x:int(x['java']),reverse=sort_stu_bool)
            show_students(sort_stu)
        elif answer =='4':
            sort_stu.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['java']),reverse=sort_stu_bool)
            show_students(sort_stu)
    else:
        print('目前没有信息')

def show_students(list):
    print('id \t\t 姓名 \t 英语  Python  JAVA  总分')
    for d in list:
        sum = d['english'] + d['python'] + d['java']
        print(
            '{0} \t {1} \t {2} \t {3} \t {4} \t'.format(d['id'], d['name'], d['english'], d['python'], d['java']) + str(
                sum))

def total():
    if os.path.exists("students.txt"): #判断文件是否存在
        with open('students.txt','r',encoding='utf-8') as file:
            total_stu=file.readlines()
            print(f'总共有{len(total_stu)}名学生')  #len函数判断列表的元素数量
    else:
        print('目前没有信息')

def show():
    if os.path.exists("students.txt"): #判断文件是否存在
        with open('students.txt','r',encoding='utf-8') as file:
            total_stu=file.readlines()
            for item in total_stu:
                d = dict(eval(item))
                sum=d['english']+d['python']+d['java']
                print('id \t\t 姓名 \t 英语  Python  JAVA  总分')
                print('{0} \t {1} \t {2} \t {3} \t {4} \t'.format(d['id'], d['name'], d['english'], d['python'],d['java']) +str(sum))
    else:
        print('目前没有信息')

if __name__ == '__main__':
    main()
