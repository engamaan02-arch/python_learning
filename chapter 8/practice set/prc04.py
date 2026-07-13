def sum(n):
    if  n ==0 :
        return 0
    return n+sum(n-1)

n = int(input("enter the number\n"))
print(f"sum of first {n} is {sum(n)}")
    