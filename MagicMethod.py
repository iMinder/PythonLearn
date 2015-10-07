# -*- coding:utf-8 -*-

# 1.定义一个父类
# 注意下面这句话，意思是下面的类都是新式的类
__metaclass__ = type

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No, thanks!'


# # 2.子类，采用未绑定的超类构造方法
# class SongBird(Bird):
#     def __init__(self):
#         Bird.__init__(self)
#         self.sound = 'Squawk!'
#     def sing(self):
#         print self.sound

# 2.子类，采用super函数来调用父类的构造方法
class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound

songBird = SongBird()
songBird.sing()
songBird.eat()
songBird.eat()