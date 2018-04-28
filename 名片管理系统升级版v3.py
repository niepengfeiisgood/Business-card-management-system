'''新名片管理系统文件版V1.2
[{"name":"niepengfei", "age":"18", "tel":'183'},
 {"name":"niepengfei", "age":'18', "tel":'183'},
 {"name":"niepengfei", "age":'18', "tel":'183'}]
功能：
1.显示菜单
2.增加名片
3.查找名片
4.删除名片
5.显示所有名片
6.退出系统，自动保存修改
注：没有重复的数据
'''

import os

#1、显示菜单
def print_menu():
    print("="*50)
    print("{:^40}".format("欢迎使用名片管理系统V1.2"))
    print('''功能：
1.显示菜单
2.增加名片
3.查找名片
4.删除名片
5.显示所有名片
6.退出系统''')
    print("="*50) 

#2、增加名片(不能添加重复的数据)
def add_card(card_list):
    one_card = {}
    one_card['name'] = input("请输入姓名：")
    one_card['age'] =  input("请输入年龄：")
    one_card['tel'] = input("请输入电话：")
    for temp in card_list:
        if temp['name']==one_card['name'] and\
            temp['age']==one_card['age'] and\
            temp['tel']==one_card['tel']:
            print("该数据已存在")
    else:
        card_list.append(one_card)

#3、查找名片
def find_card(card_list):
    find_name = input("请输入要查询的名字：")
    flag = 0
    for temp in card_list:
        if temp['name'] == find_name:
            flag = 1
            print("姓名：{}，年龄：{}，电话：{}".format(temp['name'],temp['age'],temp['tel']))
    if flag == 0:
        print("查无此人")


#4、删除名片
def del_card(card_list):
    del_name = input("请输入要删除的名字：")
    flag = 0
    for temp in card_list:
        if temp['name'] == del_name:
            flag = 1
            print("姓名：{}，年龄：{}，电话：{}".format(temp['name'],temp['age'],temp['tel']))
    if flag == 0:
        print("查无此人")
    else:
        del_age = input("请输入要删除的年龄：")
        del_tel = input("请输入要删除的电话：")
        flag2 = 0
        for temp in card_list:
            if temp['name'] == del_name and\
                temp['age'] == del_age and\
                temp['tel'] == del_tel:
                flag2 = 1
                card_list.remove(temp)
        if flag2 ==0:
            print("没有这条数据")

#5、显示所有名片
def show_card(card_list):
    print("姓名\t\t\t年龄\t\t\t电话")
    for temp in card_list:
        print("{}\t\t\t{}\t\t\t{}".format(temp['name'],temp['age'],temp['tel']))


def main():
    #用文件data.dat存储数据
    if not os.path.exists(r"E:\学习资料\python代码\名片管理系统\data.dat"):
        card_list = []
    else:
        f = open(r"E:\学习资料\python代码\名片管理系统\data.dat",'r')
        cont = f.read()
        if cont=="":
            card_list = []
        else:
            card_list = eval(cont)
        f.close()
    print_menu()
    while True:
        try:
            num = int(input("请输入功能序号(1~6)："))
            if num == 1:
                print_menu()
            elif num == 2:
                add_card(card_list)
            elif num == 3:
                find_card(card_list)
            elif num == 4:
                del_card(card_list)
            elif num == 5:
                show_card(card_list)
            elif num == 6:
                break
            else:
                print("输入错误，请重新输入")
        except:
            print("输入错误，请重新输入")
    f2 = open(r"E:\学习资料\python代码\名片管理系统\data.dat",'w')
    f2.write(str(card_list))
    f2.close()




if __name__ == '__main__':
    main()

