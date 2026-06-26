class A:
    def __init__(self):
        self.__x = 1
class B(A):
        pass
b = B()
print(b.__x)