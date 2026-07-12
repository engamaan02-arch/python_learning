#now we print a hollow a square
'''* * * * * *
   *         *  
   *         *
   *         *
   * * * * * *'''
n =int(input("enter your number \n"))
for i in range(1 ,n+1):
    print("*"  ,end="")
    print(" "  ,end="")
print("")
for i in range(1 , n):
    print("*" , end="")
    print(" "* (2*n-1) , end="")
    print("*" , end="")
    print("")

for i in range(1 , n+1):
    print("*" , end="")
    print(" " ,end="")
    
