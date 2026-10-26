class employee: #and now this is parents class
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


# class programmer:
#     company = "microsoft"
#     def show(self):
#             print(f"the name is {self.name} and the salary is {self.salary}")
#     def showlangauge(self):
#             print(f"the name is {self.name} and he is good in {self.language}")

# insteed of doing this copy and paste we use inheritence

class programmer(employee):#now this is inherited class  
    company = "microsoft"
    def showlangauge(self):
        print(f"the name is {self.name} and he is good in {self.language}")

a = employee()
b = programmer()

print(a.company ,b.company)