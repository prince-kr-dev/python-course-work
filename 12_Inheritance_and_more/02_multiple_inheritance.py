class Animal:
    def speak(self):
        print("Animal make sound")


class Dog:
    def bark(self):
        print("Dog is barking")

class Horse(Animal, Dog):
    def running(self):
        print("Horses run very fast")


a = Horse()

a.speak()
a.bark()
a.running()