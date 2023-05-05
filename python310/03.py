# str1 = int(input("请输入密码："))
# print(str1)
#
# print(type(str1))


# user_name = input("请输入名称：")
# user_level = input("您的等级为：")
#
# print(f"您好,{user_name},您的等级为：{user_level}，欢迎回来。。。")


# age = int(input("欢迎来到儿童游乐园，儿童免费，成人收费，请输入你的年龄："))
# if age >= 18:
#     print("您已成年，请购票")
# else:
#     print("您可免费进入")
# print("祝您游玩愉快")


# height = int(input("请输入身高："))
# level = int(input("请输入VIP等级："))
# day = int(input("请输入日期："))
# if height < 120:
#     print("您可免费游玩，祝您游玩愉快")
# elif level > 3:
#     print(f"尊贵的VIP{level},祝您游玩愉快")
# elif day == 1:
#     print("今天可免费游玩,祝您游玩愉快")
# else:
#     print("请购买门票，祝您游玩愉快")


# if int(input("请输入身高：")) > 120:
#     print("身高超出限制，可能无法免费游玩")
#     if int(input("请输入VIP级别：")) > 3:
#         print("vip等级足够，可免费游玩")
#     else:
#         print("请购买门票。")
# else:
#     print("欢迎，祝您游玩愉快^^")
# import random
#
# num = random.randint(1, 10)
# guess = int(input("请猜测数字："))
# if guess == num:
#     print("恭喜您，第一次就猜对了")
# else:
#     if guess > num:
#         print("猜大了")
#     elif guess < num:
#         print("猜小了")
#     guess = int(input("请猜测数字："))
#     if guess == num:
#         print("恭喜您，第二次猜对了")
#     else:
#         if guess > num:
#             print("猜大了")
#         elif guess < num:
#             print("猜小了")
#     guess = int(input("请猜测数字："))
#     if guess == num:
#         print("恭喜您，第三次猜对了")
#     else:
#         if guess > num:
#             print("猜大了")
#         elif guess < num:
#             print("猜小了")


# print('I\'m \"ok\" ')


# print("\\\n\\")
# """
# run结果为
# \
# \
# """
#
# print('''
# hello,\n
# world''')

# r''表示''内部的字符串默认不转义

# a = 'ABC'
# b = a
# a = 'DEF'
# print(b)

# print(r'''hello,
# lucy!!''')


print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
