class employee:
    company = "microsoft"
    salary = "120000"    # these three are class atributes
    language  = "python"
    def getInfo(self):
        print(f"the language is {self.language} .the salary is {self.salary}")

        # def greet(self):
        #     print("good morning") self use nha krna padhe or object nhi chiye bcz class ka use hi nhi hai toh 
        @staticmethod #yeh btatsa hai ki me self use nhi krra kiyouki mujhe object ki need nhi hai
        def greet():
            print("good morning")
            

amaan = employee()
amaan.name = "amaan"
amaan.language= "java" #this will overwrite on class 
print( amaan.name ,amaan.company , amaan.salary , amaan.language)
amaan.greet()
amaan.getInfo() #or we can use 
employee.getInfo(amaan)
