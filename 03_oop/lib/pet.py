# !/usr/bin/env python3
    # Defines the location of the Python interpreter
    # See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes
    # Blueprints => We create instances from blueprint
    # Cookie Cutter => Instances (Cookies)

# 1. ✅ Create a Pet class

# class Pet:
#     pass

# ipdb.set_trace()

    # Note: Add 'pass' to the Pet class 

# 2. ✅ Instantiate a few Pet instances

    # Compare the Pet instances. Are each of them the same object?

# 3. ✅ Demonstrate __init__ 

# self => Instance of Pet Class

class Pet:
    def __init__(self, name, age, breed, temperament):
        #attached incoming arguments to "self" (Instance)
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament

# fido = Pet("Fido", 5, "Boxer", "Tranquil")

# ipdb.set_trace()


    # Add arguments to instances  
    
    # Use dot notation to access each Pet instance's attributes 

    # Update attributes with new values

# Instance Methods

#     def say_hello(self):
#         print("Hello")

# ipdb.set_trace()

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's 
# attributes

    # Review the "self" keyword 
    
    # Invoke "print_pet_details" on an instance 
    
    # Example Terminal Ouput:
        # name: Rose
        # age: 11
        # breed: Domestic Longhair
        # temperament: Sweet

    def print_pet_details(self):
        print(f'''
            name: {self.name}
            age: {self.age}
            breed: {self.breed}
            temerapment: {self.temperament}
              
              ''')
# ipdb.set_trace()

# Object Properties => Attributes that are controlled by methods

class Owner:
    def __init__(self, age):
        self.age = age
        
# ipdb.set_trace()

    # Create an Owner class with two instance methods:

        # get_name => Retrieve Owner's name

    def get_name(self):
        print("retrieving Owner's name...")
        return self._name

    def set_name(self, name):  
        print("Setting Owner's name...") 

        if (isinstance(name, str)):

            #Assign incoming :name as "_name" for Owner instance
            self._name = name

        else: 
            print("Name must be a String")


    name = property(get_name, set_name)

ipdb.set_trace()
        # set_name => Set Owner's name

            # Ensure that Owner's name is a String

            # If not, issue warning of "Name must be a string"

    # Use property() to compile get_name / set_name and invoke them
    # whenever we access an Owner instance's name