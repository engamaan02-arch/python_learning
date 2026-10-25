class calculator:
    def __init__(self , n):
        self.n = n
    def square(self):
            print(f"the square of {self.n} is {self.n*self.n}")
    def cube(self):
            print(f"the cube of {self.n} is {self.n*self.n *self.n}")
    def squareroot(self):
            print(f"the squareroot of {self.n} is {self.n**1/2}")
    @staticmethod
    def hello():
          print("hello world")

a = calculator(4)
a.hello()
a.squareroot()
a.cube()
a.square()

         