#类名驼峰命名法

class Chinese:

    #用赋值语句，创建类的属性
    eye = 'black'

    
    def eat(self):
        print('吃饭,选择用筷子。')


me = Chinese()
print(me.eye)
me.eat()


##############################################

class Computer:



    screen = True


    def start(self):
        print()