#code for factorial of any number

n = int(input("enter your number\n"))

product = 1
for i in range(1 , n+1):
    product = product*i
print(product)