def pattern(n):
    if n == 0:
     return 0
    print("*" * n)
    pattern(n-1)

num = int(input("enter the number\n"))
pattern(num)
