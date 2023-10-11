"""

if  条件：
    代码1
else:
    代码2
    

"""

###如果条件成立，执行代码一，如果不成立，执行代码2

#============第二种==============

money = input("请输入你的钱：")
money = int(money)

if money > 500:
    print("买衣服")

else:
    print("衣服将就穿吧")


#报错 : TypeError: '>' not supported between instances of 'str' and 'int' 16行
#因为上面13行，input（）得出的是字符串，所以，16行报错，显示  字符串类型   和   数字类型   不可以用 >
# 前面加上  int   就表示生声明了数据类型  为数字类型，数字类型   >  500,可以执行

#其实也可以改成
#       money = int(input("请输入你的钱："))

