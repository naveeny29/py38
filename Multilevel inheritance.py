class A:
    def methodA(self):
        print("This Method is in class A")

class B(A):
    def methodB(self):
        print("This Method is in class B")

class C(B):
    def methodC(self):
        print("This Method is in class C")

obj = C()
obj.methodA()
obj.methodB()
obj.methodC()
