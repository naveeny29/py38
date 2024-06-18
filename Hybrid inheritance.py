class A:
    def methodA(self):
        print("This Method is in class A")

class B(A):
    def methodB(self):
        print("This Method is in class B")

class C(A):
    def methodC(self):
        print("This Method is in class C")

class D(B,C):
    def methodD(self):
        print("This Method is in class D")

obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()
