# class A:
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#         super().__init__()
#
#
# class C(A):
#     def __init__(self):
#         print("C")
#         super().__init__()
#
#
# class D(B, C):
#     def __init__(self):
#         print("D")
#         super().__init__()
#
#
# if __name__ == '__main__':
#     d = D()
#     print(D.mro())


# class A:
#     def say(self):
#         print("A")
#
#
# class B(A):
#     def say(self):
#         print("B")
#
#
# class C(A):
#     pass
#
#
# class M(C, B):
#     pass
#
#
# if __name__ == '__main__':
#     m = M()
#     m.say()
#     print(M.mro())


# class A(object):
#     print("a")
#
#
# class B(object):
#     print("b")
#
#
# class C(B, A):
#     pass
#
#
# class D(A, B):
#     pass
#
#
# if __name__ == '__main__':
#     c = C()

#     print(C.mro())
#     print(D.mro())


# s1 = set([1, 3, 2])
# s2 = set([1, 2, 3, 4, 4, 4, 3, 3, 2, 2, 2, 2, 4, 6, 7, 7])
# #
# # print(s2)
#
# s2.remove(2)
# print(s2)
# print(s1 & s2)  # 就是交集
# print(s1 | s2)  # 并集


# s1 = set([1, 3, 2], 1)
# s2 = set([1, 2, 3, 4, 4, 4, 3, 3, 2, 2, 2, 2, 4, 6, 7, 7])
# print(s1)


# a = ['b', 'c', 'a', 'd']
# a.sort()
# print(a)

# a = 'abc'
# b = a.replace('a', 'A')
# print(a)
# print(b)


# n1 = 255
# n2 = 1000
#
# print(hex(n1)) # 转为十六进制值
# print(hex(n2))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


if __name__ == '__main__':
    my_abs(4)
