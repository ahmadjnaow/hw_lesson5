class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed
    
    def bark(self):
        print(f"{self.get_name()} is barking: Woof woof!")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color
    
    def meow(self):
        print(f"{self.get_name()} is meowing: Meow meow!")


dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Gray")

print(dog.get_name())  
print(cat.get_age())   

dog.bark()  
cat.meow()  

    


