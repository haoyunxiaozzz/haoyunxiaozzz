"""
for 循环的目标是可迭代对象
字符串是可迭代的


for  变量   in   可迭代的东西：
    代码

作用：把可迭代的东西中的每一项内容拿出来，挨个的赋值给前面的变量，每一次赋值都要执行一下循环体（代码）

"""

s = '你好啊，我是赛利亚'
for c in s:
    print("这一次循环的的内容是：",c)



print('分割线-----------------------------\n')

#####################for循环想要计数，必须借助于  range  才可以###################################

###########range(n)      从0数到n，不包含n============================

for i in range(10):     #从0-9
    print(i)






print("分割线----------------------------\n")






#如果我想要从3数到9，那么就可以传进去两个参数

###########range(m,n)   从 m 数到 n   但是不包含n============================

for l in range(3,9):    #从3 - 8
    print(l)




print("分割线------------------------------------------\n")


###########range(m,n,s)     从m 数到n   ,依旧不包含n ,其中的间隔是 s

for o in range(5,30,5):         #从5 数到  30   每次间隔是5
    print(o)





"""以上的情况就和   whil 循环那里，结尾的 i + 2 就和上面这个一样,但是for循环更加简介,只需要在后面加上一个参数,就代表了一次间隔多少了


一般用的比较多的是 for 循环 , 一般 while 循环 多处用于死循环  , 因为特别的容易  ,直接

while True :     就可以了（死循环）

"""