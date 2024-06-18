class A:
    def methodA(self):
        print("This Method is in class A")

class B:
    def methodB(self):
        print("This Method is in class B")

class C:
    def methodC(self):
        print("This Method is in class C")

class D(A,B,C):
    def methodD(self):
        print("This Method is in class D")

obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()
