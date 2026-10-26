class employee:
    a=1

class programmer(employee):
    b=2

class manager(programmer):
    c =3


o = employee()
print(o.a)
# print(o.b) yeh error dega 
o1 = programmer()
print(o1.a)
print(o1.b)
# print(o.c) isme yeh error dega 
o2 = manager()
print(o2.a)
print(o2.b)
print(o2.c)
