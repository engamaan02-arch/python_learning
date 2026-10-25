from random import randint

class train:
    def __init__(self , trainNo):
        self.trainNo = trainNo

    def book(self ,fro , to):
        print(f"train is booked train no : {self.trainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"tain no{self.trainNo} is running on time ")
    def getfare(self , fro, to ):
         print(f"train fare in train no : {self.trainNo} from {fro} to {to} is {randint(222 , 5555)}")

t = train(120420)
t.book("aligarh" , "etawah")
t.getfare("aligarh"  , "etawah")
t.getstatus()