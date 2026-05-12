class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} Makes sound")
        
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Bow bow")
        
if __name__ == "__main__":
    myDog = Dog("Buddy")
    myDog.speak()
    myDog.bark()