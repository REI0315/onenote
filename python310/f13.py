# class A:
#     pass
#
#
# class B(A):  # B继承自A
#     pass
#
#
# print(isinstance(A(), A))
# print(type(A()) == A)
# print(isinstance(B(), A))
# print(type(B()) == A)
import math

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# if __name__ == '__main__':
#     print(my_abs('1'))


# def P(x, n):
#     s = 1
#     while n > 0:
#         n -= 1
#         s = s * x
#     return s
#
#
# if __name__ == '__main__':
#     print(P(2, 4))


# def add_end(L=[]):
#     L.append('END')
#     return L
#
#
#
# if __name__ == '__main__':
#     print(add_end([1, 2, 3]))
#     print(add_end(['a', 'b', 'c']))
#     print(add_end())
#     print(add_end())
#
#     # [1, 2, 3, 'END']
#     # ['a', 'b', 'c', 'END']
#     # ['END']
#     # ['END', 'END']


# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# dict1 = {'city': 'beijing', 'gender': 'female'}
#
# if __name__ == '__main__':
#     person('lucy', 30, )


# def person(name, age, *, city, gender):
#     # if 'city' in kw:
#     #     print("city")
#     # if 'job ' in kw:
#     #     print("age")
#     print(name, age, gender, city)
#
#
# if __name__ == '__main__':
#     print(person('lucy', 24, gender='female', city='beijing'))


# def f1(a, b, c=3, *args, **kwargs):
#     print('a:', a, 'b:', b, 'c:', c, 'agrs1:', args, 'kw:', kwargs)
#
#
# if __name__ == '__main__':
#     f1(1, 2)


# def mul(*args):
#     # return args[0] * args[1] # 只实现了两个参数的情况
#     result = 1
#     for i in args:
#         result *= i
#     return result
#
#
# if __name__ == '__main__':
#     print(mul(2, 3, 5))


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# if __name__ == '__main__':
#     print(fact(998))


# import requests
# import pytest
#
# url = "http://ihrm2-test.itheima.net" + "/api/sys/login"
# data_json = [{"mobile": "13800000002", "password": "123456"},  # 登录成功
#              {"mobile": "13812331241", "password": "123456"}]
#
#
# @pytest.mark.parametrize('canshu', data_json)
# def test_login(canshu):
#     response = requests.post(url=url, json=canshu, headers={"Content-Type": "application/json"})
#     if response.json().get("success") == True:
#         assert "成功" in response.json().get("message")
#     if response.json().get("success") == False:
#         assert "错误" in response.json().get("message")

# import requests
# import pytest
#
# url = "http://ihrm2-test.itheima.net/api/sys/login"
# data_json = [
#     {
#         "lll": "登录成功",
#         "data": {
#             "mobile": "13800000002",
#             "password": "123456"
#         }
#     },
#     {
#         "lll": "手机号未注册",
#         "data": {
#             "mobile": "13812331241",
#             "password": "123456"
#         }
#     }
# ]
#
# @pytest.mark.parametrize('canshu', data_json)
# def test_login(canshu):
#     response = requests.post(url=url, json=canshu["data"], headers={"Content-Type": "application/json"})
#     if response.json().get("success") == True:
#         assert "成功" in response.json().get("message")
#     if response.json().get("success") == False:
#         assert "错误" in response.json().get("message")


# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         print(a, '-->', c)
#         move(n - 1, b, a, c)
#
#
# if __name__ == '__main__':
#     move(3, 'A', ' B', 'C')

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# print(r)


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


# def trim(x):
#     while x[:1] == ' ':
#         x = x[1:]
#     while x[-1:] == ' ':
#         x = x[:-1]
#     return x
#
#
# if __name__ == '__main__':
#     x = " 这是字符串,没毛病 "
#     print(trim(x))

# L = [1, 4, 7, 8, 4, 5, 6, 9, 2, 4, 5]
#
#
# def findMaxAndMin(L):
#     maxval = L[0]
#     minval = L[0]
#     for i in L:
#         if i > maxval:
#             maxval = i
#
#         if i < minval:
#             minval = i
#     return maxval, minval
#
#
# if __name__ == '__main__':
#     print(findMaxAndMin(L))


# L = []
#
# for i in range(1, 11):
#     L.append(i * i)
# print(L)
#
# print([i * i for i in range(1, 11)])  # 列表推导式语法
#
# print([i * i for i in range(1, 100) if i % 2 == 0]

#
# print([m + n for m in 'ABC' for n in "EFG"])


# import os
#
# print([i for i in os.listdir(
#     'D:\\livepackages\\预发包\\VKPLiveBroadcast_prev0.1.9-20230314_072249\\Windows')])  # os.listdir 可以列出下方的文件和目录, ' . ' 指的是当前目录--->'./.pytest_cache/v/cache'

#
# L = ['Hello', 'World', 'IBM', 'Apple']
#
# print([l.lower() for l in L])  # 将字符串变成小写
#
# l = ['hello', 'world', 'ibm', 'apple']
# print([L.upper() for L in l])  # 将字符串全变成大写

# print([x if x % 2 == 0 else -x for x in range(1, 11)])


# print(dir(str))


# L1 = ['Hello', 'World', 18, 'Apple', None]
#
# print([x.lower() for x in L1 if isinstance(x, str) is True])


# for i in (x * x for x in range(10)):
#     print(i)

# num = input("请输入数字:")
# total = 0
# count = 0
# lst = []
# while num != 'q':
#     num1 = float(num)
#     total += num1
#     count += 1
#     num = input("请输入数字:")
# if count == 0:
#     result = 0
# else:
#     result = total / count
# print('你输入的数值的平均值为:', result)


# import statistics
#
# num = input("请输入数字:")
# lst = []
# while num != 'q':
#     lst.append(int(num))
#     num = input("请输入数字:")
# print(statistics.mean(lst))

# weight = float(input("请输入您的体重(kg):"))
# height = float(input("请输入您的身高(m):"))
#
#
# def calculate_BMI(weight, height):
#     BMI = weight / (height ** 2)
#     if BMI <= 18.5:
#         category = "偏瘦"
#     elif BMI <= 25:
#         category = "正常"
#     elif BMI <= 30:
#         category = "偏胖"
#     else:
#         category = "肥胖"
#     print(f"您的BMI分类为{category}")
#     return category
#
#
# if __name__ == '__main__':
#     print(calculate_BMI(weight, height))
