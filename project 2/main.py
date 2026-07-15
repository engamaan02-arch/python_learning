import random
print("RULES\n you should choose only one from\n ROCK  PAPER  SCISSOR")
print("ROCK WON AGAINST SCISSOR\nSCISSOR WON AGAINST PAPER\nPAPER WON AGAINST ROCK")
print("\n")
computer = random.choice(["rock" , "paper" , "scissor"])
user =input("choose one from rock / paper / scissor\n").lower()
# print(f"computer choose{computer}")

if(user==computer):
    print(f"its draw \nbcz you and computer choose {user}")
elif(user=="rock" and computer=="paper"):
    print(f"you lost !!\n computer choose {computer}\n  and u choose {user} \ntry again!!")
elif(user=="rock" and computer=="scissor"):
    print(f"you won!!\n computer choose {computer} and u choose {user}")
elif(user=="paper" and computer=="scissor"):
    print(f"you lost !!\n computer choose {computer}\n  and u choose {user} \ntry again!!")
elif(user=="paper" and computer=="rock"):
    print(f"you won!!\n computer choose {computer} and u choose {user}")
elif(user=="scissor" and computer=="rock"):
    print(f"you lost !!\n computer choose {computer}\n  and u choose {user} \ntry again!!")
elif(user=="scissor" and computer=="paper"):
    print(f"you won!!\n computer choose {computer} and u choose {user}")
else:
    print("invalid output")

