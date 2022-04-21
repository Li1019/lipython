# =======================
# class_all
# Author : Li
# 2022/04/17
# 16:54
encoding = 'utf-8'

# =======================
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def perimeter(self):
#         return (self.length + self.width) * 2
#
#     def area(self):
#         return self.length * self.width
#
#     @classmethod  # 装饰器，声明后面的方法是类方法
#     def feature(cls):
#         print('width = length, and every corner is 90')
#
#     @staticmethod  # 装饰器，声明后面的方法是静态方法，不受class控制，挂靠在这个类里
#     def sum_data(num1, num2):
#         return num1 + num2
#
#
# Rectangle.feature()  # 类的方法不需要实例化，可以直接调用
# print(Rectangle.sum_data(1, 3))  # 静态方法不需要实例化，可以直接调用
#
# rectangle1 = Rectangle(10, 8)
# print(rectangle1.perimeter())
# print(rectangle1.area())
#
# # type()查看对象是方法还是函数, return is type
# print(type(rectangle1.perimeter))
# print(type(rectangle1.area))
# print(type(rectangle1.sum_data))
#
# # inspect, 判断对象是否是某个方法，return是布尔型
# import inspect
#
# print(inspect.ismethod(rectangle1.feature))
# print(inspect.isfunction(rectangle1.feature))
# print(inspect.ismethod(rectangle1.feature))
# print(inspect.isfunction(rectangle1.sum_data))
#
#
# # 正方形的class，继承 Retangle
# # 完全继承
# class Square(Rectangle):
#     pass
#
#
# squ1 = Square(6, 6)
# print(squ1.area())
#
#
# # 部分继承
# class Square_new(Rectangle):
#     def __init__(self, side):
#         self.length = side
#         self.width = side
#
#     @classmethod
#     def feature(cls):
#         super().feature()
#         print('width and length is same')
#
# squ2 = Square_new(7)
# print(squ2.area())
# print(squ2.perimeter())
# squ2.feature()


# 多个父类
# class Money1:
#     def money(self):
#         print('1')
#
#
# class Money2:
#     def money(self):
#         print('2')
#
#
# class Human(Money1, Money2):  # 多个父类，同名方法按继承顺序优先继承
#     pass
#
#
# human1 = Human()
# human1.money()

# class Triangle:
#     def __init__(self, width, height, third_line):
#         self.width = width
#         self.height = height
#         self.third_line = third_line
#
#     def perimeter(self):
#         return self.width + self.height + self.third_line
#
#     def area(self):
#         return (self.width * self.height) / 2
#
#
# triangle1 = Triangle(1, 2, 3)
# print(triangle1.perimeter())
# print(triangle1.area())


# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def perimeter(self):
#         return 3.14 * 2 * self.r
#
#     def area(self):
#         return 3.14 * self.r * self.r
#
#
# circle1 = Circle(10)
# print(circle1.perimeter())
# print(circle1.area())


# class Animal:
#     def __init__(self, animal):
#         self.animal = animal
#
#     def bray(self):
#         if self.animal == 'dog':
#             print('won!won!')
#         if self.animal == 'cat':
#             print('mua...mua...')
#
#
# test_animal = 'dog'
# animal = Animal(test_animal)
# animal.bray()
#
# # hasattr
# print(hasattr(Animal, 'bray'))  # class name, 检查class有没有方法和属性, return is boolean
#
# # getattr
# print(getattr(Animal, 'bray'))  # class name, 检查class有没有方法和属性, return: 方法/属性, if can't get, return error
#
# # class name, 检查class有没有方法和属性, return: 方法/属性, if can't get, return 3rd part
# print(getattr(Animal, 'bray1', 'not found'))

# setattr
# change class 属性 value, if not found, then create a new 属性

# class Class_test:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#
#
# setattr(Class_test, 'a', 20)
# print(Class_test.a)
#
# cls1 = Class_test()
# setattr(cls1, 'b', 88)
# print(cls1.b)
#
# setattr(cls1, 'c', 32)  # if don't exit this parameter, then create a new one
# print(cls1.c)
#
# setattr(Class_test, 'd', 123)
# print(Class_test.d)

# 单利模式
# 一个类可以生成任意个模式，单利模式只生成一个实例

# class Single:
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'obj'):
#             cls.obj = object.__new__(cls)
#         return cls.obj
#
#
# s1 = Single()
# s2 = Single()
# print(s1 == s2)

# class Restaurant:
#     def __init__(self):
#         pass
#
#     def maladoufu(self):
#         return 'ma la dou fu'
#
#     def xianglarousi(self):
#         return 'xiang la rou si'
#
#     def huoguo(self):
#         return 'hot pot'
#
#
# customer = Restaurant()
#
# i = 0
# while (i < 9):
#     menu = input('Please order dish: ')
#     if hasattr(customer, menu):
#         print(f'We will prepare {menu} for you')
#         break
#     else:
#         print(f"We don't provide {menu}, please order others")
#     i += 3


# 私有属性/方法
# 不能被外部调用，也不能被子类继承
# 属性/方法前面有__的是私有，前后都有的不是私有
#
# class Class_private:
#     __str1 = 'private'  # 私有属性
#     str2 = 'public'  # NOT 私有属性
#
#     def __method1(self):
#         print('This is private method')
#
#     def method2(self):
#         print('this is not private method')
#
#
# cls1 = Class_private()
# print(cls1.str2)
# print(cls1.method2())
# # print(cls1.__str1)  # error occurs


# class Class_property:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def method_property(self):
#         return self.a * self.b
#
# cls1 = Class_property(1,2)
# print (cls1.method_property)  # 调用property方法和调用参数是一样的，最后不需要写()

# 类的多态
# 不同的class，但是 有同名的方法，比如cat/dog都会叫，方法【叫】相同，但是类不同
#
# class Dog:
#     def bray(self):
#         print('wonwonwon!')
#
#
# class Cat:
#     def bray(self):
#         print('miaomiao')
#
#
# dog = Dog()
# cat = Cat()
#
# # 调用多态类的方法的时候，写一个函数来调用，参数是实例
# def animal_bray(animal):
#     animal.bray()
#
#
# animal_bray(dog)
# animal_bray(cat)

# import random
#
#
# class Restaurant:
#     def cooker(self):
#         print('cooker is Pan')
#
#
# class Yuxiangrousi(Restaurant):
#     def __init__(self):
#         self.i = random.randint(3, 20)
#
#     def cook(self):
#         print(f'will provide yuxiangrousi in {self.i} minutes')
#
#
# class Mapodoufu(Restaurant):
#     def __init__(self):
#         self.i = random.randint(3, 20)
#
#     def cook(self):
#         print(f'will provide mapodoufu in {self.i} minutes')
#
#
# class Huoguorou(Restaurant):
#     def __init__(self):
#         self.i = random.randint(3, 20)
#
#     def cook(self):
#         print(f'will provide huoguorou in {self.i} minutes')
#
#
# customer1 = Mapodoufu()
# customer2 = Yuxiangrousi()
# customer3 = Huoguorou()
#
#
# def order_menu(obj):
#     obj.cook()
#     obj.cooker()
#
#
# order_menu(customer1)
# order_menu(customer2)
# order_menu(customer3)
