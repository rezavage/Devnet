class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name} ")


john = Person("john taheri")
print(john.name)
john.talk()

bob = Person("Bob rogers")
bob.talk()

