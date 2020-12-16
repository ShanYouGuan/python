class A(object):
    def foo(self):
        print("enter A")
        super(A, self).foo()
        print("leave A")


class B(object):
    def foo(self):
        print("enter B")
        super(B, self).foo()
        print("leave B")


class C(A):
    def foo(self):
        print("enter C")
        super(C, self).foo()
        print("leave C")


class D(A):
    def foo(self):
        print("enter D")
        super(D, self).foo()
        print("leave D")


class E(B,C):
    def foo(self):
        print("enter E")
        super(E, self).foo()
        print("leave E")


class F(E, D):
    def foo(self):
        print("enter F")
        super(F, self).foo()
        print("leave F")



f = F()
f.foo()
print(F.__mro__)