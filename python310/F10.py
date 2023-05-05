# class A(object):
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
# if __name__ == "__main__":
#     d = D()
#     print(D.mro())


class A(object):
    def __init__(self):
        print("A")


class X():
    def __init__(self):
        print("x")


class B(X):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("c")
        super().__init__()


class D(C, B):
    def __init__(self):
        # super().__init__()
        print("zuihou D")
        super().__init__()


if __name__ == '__main__':
    d = D()
