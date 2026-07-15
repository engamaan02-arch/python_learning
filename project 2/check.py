import random

num = random.randint(0,2)
#user input
user= (input("select one from rock/ paper /scissor\n"))
if(user=="rock"):
    a = int(2)
elif(user =="paper"):
    b = int(1)
elif(user=="scissor"):
    c = int(0)
else:
    print("invalid input")


# print("random number : " , num)
#this is random computer output:
if(num==0):
    c1 =("scissor")
elif(num== 1):
    b1 =("paper")
elif(num == 2):
    a1 =("rock")
else:
    print("none")

#this is possiblity for mechanism
if(a == num and num==2):
    print(f"its draw!!\nyou and computer both choose {a1}")
elif(b == num and num ==1):
    print(f"you and computer both choose {b1}")
elif(c == num and num ==0):
    print(f"you and computer both choose {c1}")
elif(user=="paper" and num==2):
    print(f"you won !!\n computer choose{a1} and\n u choose paper")
elif(user=="paper" and num==0):
    print(f"you lost!!\n computer choose{c1} and\n u choose paper\n try again!!!")
elif(user=="scissor" and num ==1):
     print(f"you won !!\n computer choose{b1} and\n u choose scissor")
elif(user=="scissor" and num==2):
     print(f"you lost !!\n computer choose{a1} and\n u choose scissor\n try again!!!")
elif(user== "rock" and num ==0):
     print(f"you won !!\n computer choose{c1} and\n u choose rock")
elif(user== "rock" and num==1):
     print(f"you lost !!\n computer choose{b1} and\n u choose rock\n try again!!!")
else:
    print("eroor wrong input")
    
