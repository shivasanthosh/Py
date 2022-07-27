class dog:
    def bark(self):
        print("boww boww")

class emp:
    def __init__(self,name):
        self.name=name

    def print_name(self):
        print("Hey ",self.name)


kaala= dog()

print(dir(emp))

kaala.bark()