def pattern(n):
    if n == 0:
     return 0
    for i  in range(1 , n+1):
       print("*" * ((n+1)-i), end="")
       print("")
n = int(input("enter the number\n"))

pattern(n)