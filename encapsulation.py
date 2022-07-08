class Person():
    def __init__(self, name, age) -> None:
        self.__name = name  # private properties
        self.__age = age    

    @property
    def Name(self): # get
        return self.__name

    @property
    def Age(self):
        return self.__age

    @Name.setter #set
    def Name(self, value):
        if value == 'Aaku':
            self.__name = "DEFAULT NAME"
        else:
            self.__name = value

    @staticmethod # <- I dont need an object to call this method
    def myMethod():
        print("Hello World!")

Person.myMethod()

p1 = Person('Martin', 15)
print(p1.Name, p1.Age)


