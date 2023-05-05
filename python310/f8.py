# def login():
#     username = input("请输入登录id：\n")
#     pwd = input("请输入密码:\n")
#     if username == 'rei' and pwd == '123456':
#         return '1234567890-='
#     # else:
#     #     print('请登录')
#
#
# def profile(session):
#     if session == '1234567890-=':
#         print('欢迎访问个人主页')
#     else:
#         print('登录已过期,请重新登录')
#
#
# profile(login())


# def f():
#     name = '父函数'
#
#     def f1():
#         name = '子函数'
#         print(name)
#
#     return f1()
#
#
# f()


# f1 = lambda a, b: a + b
#
# print(f1(1, 3))

# age = 6
# # 三目运算 x if 布尔表达式 else y  布尔表达式为TRUE返回x 为FALSE返回y
# print('TRUE这边') if age > 5 else print('FALSE另一边')


# login = lambda username, password: print("登录成功") \
#     if username == 'rei' and password == '12345' else print("登录失败")
#
# login('rei', '12345')


# data = lambda **kwagrs: dict(sorted(kwagrs.items(), key=lambda item: item[0]))
#
# print(data(name='李华', age=12))


# cls = ['cls2', 'cls2', 'cls3']
# print(len(cls))
#
# print(cls[-1])
# cls.append('cls4')
# print(cls)
#
# cls.insert(0, 'cls1')
# print(cls)
#
# cls1 = [1, 2, 3, [4, 5, 6], 7, 8, 9]
#
# print(cls1[3])


# tuple1 = (1, 3, [5, 7], 9)
#
# tuple1[2][0] = 4
# tuple1[2][1] = 6
#
# print(tuple1)
#
# # 变的不是tuple的元素，而是list的元素


# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])


# s = int(input('生日为:\n'))
#
# if s < 2000:
#     print('00前')
# else:
#     print('00后')


# height = 1.75
# weight = 80.5
#
# bmi = weight / height ** 2
# print(bmi)
#
# if weight / height ** 2 < 18.5:
#     print('过轻')
# elif 25 >= weight / height ** 2 >= 18.5:
#     print('正常')
# elif 28 >= weight / height ** 2 >= 25:
#     print('过重')
# elif 32 > weight / height ** 2 >= 28:
#     print('肥胖')
# else:
#     print('严重肥胖')


# sum = 0
# for i in range(101):
#     sum += i
# print(sum)


# sum = 0
# n = 100
# while n > 0:
#     sum += n
#     n -= 2
# print(sum)

n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n += 1
# print('END')


# while n <= 100:
#     n += 1
#     if n % 2 == 0:
#         continue
#     print(n)


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print('Bob' in d)

print(d.get('tom', -1))
