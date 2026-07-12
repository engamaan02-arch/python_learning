no = int(input("enter your number\n"))
i = 2
for i in range( 2 , no):
    if(no%i) == 0:
        print("your number is not prime")
        break
else:
    print("your number is prime")
        


    



