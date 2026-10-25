class employee:
    company = "microsoft"
    salary = "120000"    # these three are class atributes
    language  = "python"

    def __init__(self , name , salary , language ):
        self.name = name 
        self.salary = salary # they are instant attribute now directly object me likh sakte hai 
        self.language = language

    def getInfo(self):
        print(f"the language is {self.language} .the salary is {self.salary}")

        # def greet(self):
        #     print("good morning") self use nha krna padhe or object nhi chiye bcz class ka use hi nhi hai toh 
        @staticmethod
        def greet():
            print("good morning")
            

amaan = employee("amaan" ,1300000, "javscript")
 
print( amaan.name ,amaan.company , amaan.salary , amaan.language)


