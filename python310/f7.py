# def add(a, b, c, d):
#     print(a + b + c + d)
#
#
# add(1, 2, 3, 4)

# 文件的路径以及具体的文件\模式\编码\
# open('log.txt', 'w', encoding='utf8')


# def f1(*args, **kwargs):  # 一个星号代表元组,两个星号代表字典
#     print(args, kwargs)
#
#
# f1([1, 2, 3])
# f1('a')
# f1(name='lihua')
# f1(dict1={'name': 'lihua'})

# ([1, 2, 3],) {}
# ('a',) {}
# () {'name': 'lihua'}
# () {'dict1': {'name': 'lihua'}}


"""
需求为:对请求参数进行ASCII排序
排序后进行md5加密
"""


# from operator import itemgetter
#
#
# # dict1 = {'name ': '李华', 'age': 18}
# def data(**kwargs):
#     return dict(sorted(kwargs.items(), key=itemgetter(0)))
#     # return dict(sorted(kwargs.items(), key=lambda item: item[0]))
#
#
# dict1 = {'name ': '李华', 'age': 18, 'address': '北京市', 'work': 'tester'}
#
# print(data(**dict1))  # ** 运算符可以将字典转换为关键字参数传递给函数


