import random

def game():
    print("you are playing a game")
    score = random.randint(1, 100)
    #fetch the highscore
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"your score is {score}")
    if (score>highscore ):
        print("congratulations you have the high score")
        #update the highscore
        with open("highscore.txt", "w") as f:
            f.write(str(score))
            
    return score


game()