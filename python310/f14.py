# class CuteCat:
#     def __init__(self, cat_name, cat_age, cat_color):
#         self.name = cat_name
#         self.age = cat_age
#         self.color = cat_color
#
#     def speak(self):
#         print("喵" * self.age)


# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.id = student_id
#         self.grades = {'语文': 0, '数学': 0, '英语': 0}
#
#     def set_grade(self, course, grade):
#         if course in self.grades:
#             self.grades[course] = grade
#
#     def print_grade(self):
#         print(f"学生的姓名为{self.name},学号为{self.id}")
#         for course in self.grades:
#             print(f"{course} : {self.grades[course]}")
#
#
# if __name__ == '__main__':
#     chen = Student("小陈", '001')
#     chen.set_grade("数学", 95)
#     chen.set_grade("语文", 100)
#     chen.print_grade()


# 类继承练习:人力系统
# 员工分为两类: 全职员工 FullTimeEmployee、兼职员工 PartTimeEmployee。
# 全职和兼职都有“姓名 name"、“工号 id”属性,
# 都具备"打印信息 print_info” (打印姓名、工号) 方法。
# 全职有"月薪 monthly_salary"属性，
# 在兼职有"日薪 daily_salary"属性、“每月工作天数 work_days"的属性
# 全职和兼职都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样


# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def print_info(self):
#         print(f"员工的姓名为{self.name},员工的工号为{self.id}")
#
#
# class FullTimeEmployee(Employee):
#     def __init__(self, name, id, monthly_salary):
#         super().__init__(name, id)
#         self.monthly_salary = monthly_salary
#
#     def calculate_monthly_pay(self):
#         return self.monthly_salary
#
#
# class PartTimeEmployee(Employee):
#     def __init__(self, name, id, daily_salary, work_days):
#         super().__init__(name, id)
#         self.daily_salary = daily_salary
#         self.work_days = work_days
#
#     def calculate_monthly_pay(self):
#         return self.daily_salary * self.work_days
#
#
# if __name__ == '__main__':
#     jack = FullTimeEmployee('jack', '00001', 20000)
#     rose = PartTimeEmployee('rose', '00002', 500, 30)
#
#     jack.print_info()
#     rose.print_info()
#     print(f"jack的月薪为{jack.calculate_monthly_pay()}")
#     print(f"rose的月薪为{rose.calculate_monthly_pay()}")


# with open("./log.txt", "r", encoding="utf8") as file:
#     '''方法1'''
#     # lst = file.readlines() # 读全部,返回列表 -- > 结合for循环分别打出列表中的内容
#     # for i in lst:
#     #     print(i)
#     '''方法2'''
#     # print(file.read())  # 读全部,返回字符串
#     '''方法3'''
#     line = file.readline()  # 读取一行 -- > 结合while循环,判断读到的不为None的情况下,持续读取文件内容
#     while line != "":
#         print(line)
#         line = file.readline()


# with open("log.txt", 'w', encoding='utf8') as f:
#     f.write('hello!\n')
#     f.write('yoho')
#
#
# with open("log.txt", 'a', encoding='utf8') as f:
#     f.write('111!\n')

#
# with open("poem.txt", "w", encoding='utf8') as f:
#     f.write(" 我欲乘风归去，\n 又恐琼楼玉宇,\n 高处不胜寒。\n")
#
# with open("poem.txt", "a", encoding='utf8') as f:
#     f.write(" 起舞弄清影，\n 何似在人间。")
#
# 用r+ 则既可以读也可以写


# def bubble_sort(arr):
#     n = len(arr)
#     # 遍历数组
#     for i in range(n):
#         # 每一轮遍历后，最后 i 个元素已经排好序了，不需要再比较
#         for j in range(0, n - i - 1):
#             # 如果前一个元素比后一个元素大，则交换它们的位置
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
#
# # 测试
# arr = [64, 34, 25, 12, 22, 11, 90]
# print(list(bubble_sort(arr)))
# print("排序后的数组：")
# for i in range(len(arr)):
#     print("%d" % arr[i])
#
#
# lst = [1, 2, 3, 4, 5]
#
# print(list(map(lambda a: a + 100, lst)))      # 对可迭代对象中的每一个元素应用相同的函数,将其返回值作为结果的一个元素,最终返回一个迭代器对象
# print(list(filter(lambda a: a > 1, lst)))    # 过滤
#
# lst2 = []
#
# for i in filter(lambda a: a > 1, lst):  # map\filter函数返回的为迭代器对象,需转换为list或是使用for循环遍历迭代器对象
#     lst2.append(i)
# print(lst2)
#
#
# def getinfo(func):
#     def inner():
#         print("---第一行---")
#         func()
#
#     return inner
#
#
# @getinfo
# def f1():
#     print("---可能是第二条---")
#
#
# @getinfo
# def f2():
#     print("---也可能是第二条---")
#
#
# if __name__ == '__main__':
#     f2()
#
#
# from collections.abc import Iterable
#
# print(isinstance('ABC', Iterable))  # True
# print(isinstance({"name": "jack", "age": 18}, Iterable))  # True
# print(isinstance([1, 2, 3], Iterable))  # True
# print(isinstance(123, Iterable))  # False
#
#
# def findMinAndMax(L):
#     lenl = len(L)
#     if L == "":
#         return None, None
#     if lenl == 1:
#         return L[0], L[0]
#     max1 = min1 = L[0]
#     for i in range(lenl):
#         if L[i] > max1:
#             max1 = L[i]
#         elif L[i] < min1:
#             min1 = L[i]
#     return max1, min1
#
#
# if __name__ == '__main__':
#     L = [1, 4, 6, 4, 5, 6, 9, 0, 3]
#     print(findMinAndMax(L))
#
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [l1.lower() for l1 in L1 if type(l1) == str]
#
# if __name__ == '__main__':
#     print(L2)
#     if L2 == ['hello', 'world', 'apple']:
#         print('测试通过!')
#     else:
#         print('测试失败!')
