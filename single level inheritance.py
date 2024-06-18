class A:
    def methodA(self):
        print("This Method is in class A")

class B(A):
    def methodB(self):
        print("This Method is in class B")

obj = B()
obj.methodA()
obj.methodB()
