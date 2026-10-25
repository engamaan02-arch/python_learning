class employee:
    company = "microsoft"
    salary = "120000"    # these three are class atributes
    language  = "python"

    def __init__(self):#yeh special method hai isko call karne ki zarurat nhi hai yeh khud hi ca;l hojata hain jaise hi ek naya object banega 
        print("i am creating an object")
    def getInfo(self):
        print(f"the language is {self.language} .the salary is {self.salary}")

        # def greet(self):
        #     print("good morning") self use nha krna padhe or object nhi chiye bcz class ka use hi nhi hai toh 
        @staticmethod
        def greet():
            print("good morning")
            

amaan = employee()
amaan.name = "amaan"
amaan.language= "java" #this will overwrite on class 
print( amaan.name ,amaan.company , amaan.salary , amaan.language)

amaan.getInfo() #or we can use 
employee.getInfo(amaan)
