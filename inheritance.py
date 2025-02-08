class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class B(A):
    pass

obj_a = A(1,2)
obj_b = B(3,4)
print(obj_a.a)
print(obj_b.a)