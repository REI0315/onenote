class A(object):

    def __init__(self):
        # super().__init__()
        print("A")


class X(object):
    sun_x = 'x'

    def __init__(self):
        # super().__init__()
        print("x")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("c")
        super().__init__()


class D(A, X):
    def __init__(self):
        print("zuihou D")
        super().__init__()


if __name__ == '__main__':
    d = D()
