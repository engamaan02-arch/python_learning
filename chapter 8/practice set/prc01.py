def f1():
    a = int(input("enter your number\n"))
    b = int(input("enter your number\n"))
    c = int(input("enter your number\n"))
    if(a>b and a>c):
        print(f"{a} is the greatest number")
    if(b>a and b>c):
        print(f"{b} is greatest number among")
    if(c>a and c>b):
        print(f"{c} is greatest number in among")

f1()    
