# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")


# Create object of child class
d = Dog()

d.speak()   # inherited from Animal
d.bark()    # own method
