class A():
    def __init__(self,n):
        self.num=n
    def __add__(self, other):
        return self.num+other
    def __str__(self):
        return "111111"
a=A(3)
print(a.__add__(4))
print(a)
