from random import randint
#if i change self with slf or any other thing what will happend lets see
class train:
    def __init__(slf , trainNo):
        slf.trainNo = trainNo

    def book(slf ,fro , to):
        print(f"train is booked train no : {slf.trainNo} from {fro} to {to}")
    def getstatus(slf):
        print(f"tain no{slf.trainNo} is running on time ")
    def getfare(slf , fro, to ):
         print(f"train fare in train no : {slf.trainNo} from {fro} to {to} is {randint(222 , 5555)}")

t = train(120420)
t.book("aligarh" , "etawah")
t.getfare("aligarh"  , "etawah")
t.getstatus()

#nothing is happend bcz its just a parameter we can use any word but self look clean 