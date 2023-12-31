""" 
Break:      跳出整个循环    让当前的循环立即停止
continue:   跳出本次循环
"""


#发送给下路，发送什么呢？发送这个content  
#打印语句，可以通过逗号隔开，把这两个一起打印出来
#先给下路发送什么东西，然后把content接上去


while True:
    content = input("请输入你要喷的内容(按q结束喷人):")
    if content == 'q':
        break

    print("发送给下路两个卧龙凤雏:",content)

print('测试一下,break之后只是结束了本次循环')

#注意，这里的 break 是结束本次循环，并不是结束程序




print('分割线=======================================\n')
print('分割线=======================================\n')

""" continue  :停止当前本次循环,继续执行下一次循环"""


#从1数到10

# i = 1
# while i <= 10 :
#     if i == 4:        #需要在这里加上   i = i + 1
#         continue
#     print(i)
#     i = i + 1

"""
输出的结果是到3就停止了, 那么进行分析代码,  当i= 4时  ,  i <= 10    i == 4  跳过本次循环
但是,要注意, i 没办法加1 ,  所以这里的i就一直是4  ,然后小于10 ,然后continue (跳出本次循环)
程序就卡在这里了,这个循环就在第二行到第四行绕上圈了   判断是否小于四 ----->   continue跳出本次循环
"""

#所以想要程序继续跑下去，但是不要4这个数，那么就需要在这个continue（跳出本次循环）的前面加上  i = i + 1


i = 1
while i <= 10:
    if i == 4:
        i = i + 1
        continue        #终止当前本次循环，继续执行下一次循环
    print(i)
    i = i + 1




#场景：
#break : 假如，在我处理数据的时候，发现其中有一个数据会直接影响我最终的结果，我不需要再需要计算了，那就可以直接break，直接停止这个循环，直接得我最终得结果了

#continue :  假如我在做数据检索的时候，发现数据库中有些无效数据，无效数据不需要处理，所以就直接continue

"""列子
如果进行发工资，但是有100个人，挨个循环着发工资肯定不现实，万一其中有人离职了
所以，这个时候就可以用continue

if 人是否离职(离职）：
    continue 
if 在职：
    发工资

"""
