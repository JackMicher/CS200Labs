# Jack Micher
# 9/3/2020
# CS/IT 200-03

'''
    Python File for CS/IT 200 Lab 0
    Part 2: Dog
'''

class Dog:
    
    def __init__(self, name="N/A", age=0, breed="N/A"):
        self.name = name
        self.age = age
        self.breed = breed
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_breed(self, breed):
        self.breed = breed
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_breed(self):
        return self.breed

def main():
    # Create dog1 object "Doge" from the class Dog
    dog1 = Dog(name="Doge",age=777,breed="Shiba Inu")
    
    # Get info of the dog1 object
    print("Meet my dog: " + dog1.get_name())
    print("Age of " + dog1.get_name() + ": " + str(dog1.get_age()))
    print("Breed of " + dog1.get_name() + ": " + dog1.get_breed())
    
    # That age doesn't seem right, and that name is very silly
    # Let's change that using the set methods
    
    dog1.set_name("Terry")
    dog1.set_age(10)
    
    # Print info of dog1 object again
    print('-------------------')
    print("Meet my dog: " + dog1.get_name())
    print("Age of " + dog1.get_name() + ": " + str(dog1.get_age()))
    print("Breed of " + dog1.get_name() + ": " + dog1.get_breed())
    
if __name__ == '__main__':
    main()