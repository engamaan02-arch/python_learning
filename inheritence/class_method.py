# class employee:
#     a = 1
#    
#     def show(self):
#         print(f"the class value of a is {self.a}")

# e = employee()
# e.a = 45

# e.show()

# iska result 45 aaiga 


class employee:
    a = 1
    @classmethod #yeh aapko class attribute dhikaiga iske bina instant attribute dhikata hai 
    def show(cls):
        print(f"the class value of a is {cls.a}")

e = employee()
e.a = 45

e.show()