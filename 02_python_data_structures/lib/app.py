# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

#MUTABLE
# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name

# print(pet_names[0])
# prints fitst name in list

# print(pet_names[-1])
# prints last name in list


#3. ✅ Return all pet names beginning from the 3rd index

#inclusive
# print(pet_names[3:])
#returns list starting from INDEX 3 to the last

#4. ✅ Return all pet names before the 3rd index

# EXCLUSIVE
# print(pet_names[:3])
#prints list starting from the beginning of the list up to INDEX 3


#5. ✅ Return all pet names beginning from the 3rd index and up to the 7th

# print(pet_names[3:8]) # INCLUSIVE - includes the index of 8
# prints starting at INDEX 3 to 7
# Luke => 3
# Tome => 7

# print(pet_names[3:7]) #EXCLUSIVE - excludes the index of 7
# Luke => 3
# Spot => 6



#6. ✅ Find the index of a given element => .index()

# print(pet_names.index("Rose"))
# => 0

# print(pet_names.index("Paul"))
# => 9

# print(pet_names.index("Bud"))
# => ValueError

#7. ✅ Reverse the original list => .reverse()

#DESTRUCTIVE
# DEMONSTRATES THE MUTABILITY OF LISTS
# print(pet_names.reverse())  # => None
# print(pet_names)

#8. ✅ Return the frequency of a given element => .count()

# print(pet_names.count("Rose"))
# counts the amount of "Rose" in the list 

# Updating Lists
#9. ✅ Change the first name to all uppercase letters => .upper()

# print(pet_names[0].upper())
# pulling the first in list with bracket notation and making it uppercase. 

# some_variable = pet_names[0].upper() # reassigning the first in list and making uppercase
# print(pet_names)
# print(some_variable) # storing that one idividual name to a variable


#10. ✅ Append a new name to the list => .append()
#MUTATES (DESTRUCTIVE)
# pet_names.append("Bud") # adds new name to END of list.
# print(pet_names)


#11. ✅ Add a new name at a specific index => .insert()
#takes two arguments
# argument 1 => Index
# argument 2 => Value

# pet_names.insert(0,"Bud")
# pet_names.insert(-1,"Memo") # adds to the end of the list minus one. (second to last) use APPEND FOR LAST OF LIST
# print(pet_names)


#12. ✅ Add two lists together => +

# new_pet_list = pet_names + ["Memo", "Ivy"] # COMBINING PET_NAMES LIST WITH "MEMO", "IVY" 
# print(new_pet_list)

# number_list = [1,2,3] + [4,5,6]
# print(number_list)


#13. ✅ Remove the final element from the list => .pop()

# print(pet_names)

# # Mutative (DESTRUCTIVE)
# pet_names.pop()
# print(pet_names)


#14. ✅ Remove element by specific index => .pop()

# print(pet_names)
# pet_names.pop(0) # removes name from the INDEX provided
# print(pet_names)


#15. ✅ Remove a specific element => .remove()

# print(pet_names)
# pet_names.remove("Rose") # removes by the Name provided
# print(pet_names)

#IF MULTIPLES OF THE SAME NAME ARE IN THE LIST, REMOVE WILL TARGET THE FIRST NAME IN THE LIST TO REMOVE


#16. ✅ Remove all pet names from the list => .clear()

# print(pet_names)
# pet_names.clear() # clears the whole list (empty)
# print(pet_names)


#Tuple
# 📚 Review:
# Why are tuples Immutable?

    #QUESTION
    # what advantages does this provide for us? In what situations would tuples serve us?
    #ANSWER
    # Helps us preserve our data, keep it from being changed or altered in any way. 

    # Mutable, Immutable <=> Changeable, Unchangeable

#17. ✅ Create a Tuple of 10 pet ages => () 

pet_ages = (1,2,3,4,5,6,7,8,9,10)


#18. ✅ Print the first pet age => []

# print(pet_ages[0]) # first  in list
# print(pet_ages[-1]) #last in list

# Testing Mutability 
#19. ✅ Attempt to remove an element with ".pop" (should error)

# pet_ages.pop()     # gives AttributeError


#20. ✅ Attempt to change the first element (should error) => []

# pet_ages[0] = 2    # gives TypeError


# Tuple Methods
#21. ✅ Return the frequency of a given element => .count()

# print(pet_ages.count(1))    # counts how many elements are in list

#22. ✅ Return the index of a given element  => .index()

# print(pet_ages.index(1))    # prints the INDEX of the elemnt passed through. find the first one in the list 

#23. ✅ Create a Range 
# Note:  Ranges are primarily used in loops

# print(range(60)) # ranges 0 -60



# Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}

# Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
pet_info_spot = {'name':'Spot', 'age':23, 'breed':'dalmation'}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
# pet_info_spot_1 = {'name': 'Spot', 'age': 25, 'breed': 'boxer'}
# pet_info_spot_2 = dict(name='Spot', age=25, breed='boxer')

#BOTH PRINT THE SAME = {'name': 'Spot', 'age': 25, 'breed': 'boxer'}
#TWO DIFFERENT WAYS OF WRITING IT
# print(pet_info_spot_1)
# print(pet_info_spot_2)

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info_rose['name'])
# print(pet_info_rose['temperament']) # looking for something thats not there
# KeyError: 'temperament'


#28. ✅ Print the pet attribute of "age" using ".get"

    # Note: ".get" is preferred over bracket notation in most cases 
    # because it will return "None" instead of an error

# print(pet_info_rose.get('temperament')) #returnes None
# print(pet_info_rose.get('temperament', 'Attribute Not Found!')) #returnes None with second argument as Attribute Not Found!


# Updating 
#29. ✅ Update Rose's age to 12 => []
# print(pet_info_rose)
# pet_info_rose['age'] = 12  # updates age in list
# print(pet_info_rose)


#30. ✅ Update Spot's age to 26 => .update({...})

# print(pet_info_spot)
# pet_info_spot.update({"age": 26}) # another way to update key value in list.
# print(pet_info_spot)


# Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []
# print(pet_info_rose)
# del pet_info_rose["age"]
# print(pet_info_rose)


#32. ✅ Delete Spot's age using ".pop"

# print(pet_info_rose)
# pet_info_rose.pop("age")
# print(pet_info_rose)


#33. ✅ Delete the last item for Rose using "popitem()"

# print(pet_info_rose)
# pet_info_rose.popitem() #popitem removes the last key: value in dictionary
# print(pet_info_rose)


# Loops 
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range

# for num in range(10):
#     print(num)


#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number

# 50 => start of range
# 60 => end of range
# 2 => increments by 2 from 50 - 60
# for num in range(50, 60, 2): 
#     print(num)

#36. ✅ Loop through the "pet_info" list and print every dictionary 
# for pet in pet_info:
#     print(pet)


#37. ✅ Create a function that takes a list a parameter 
    # The function should use a "for" loop to loop through the list and print each item 
    # Invoke the function and pass it "pet_names" as an argument

# def loop_through_list(list):
#     for pet in list:
#         print(pet)

# loop_through_list(pet_info)


#38. ✅ Create a function that takes a list as a parameter
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 

# def demonstrate_while(list):
#     counter = 0 

#     while(counter < len(list) -1):
#         counter += 1

#     return counter
    
# print(demonstrate_while(pet_names))


#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'

# def update_pet_age(list, name, age):    
#     index = 0
#     while(list[index]["name"] != name and index < len(list) -1):
#         index =+ 1

#         if (list[index]["name"] == name):
#             list[index]["age"] = age

#             # return list[index]   # returns only the idividual element/dictionary
#            # return list   # returns the whole list 
        
#         else:
#             return "Pet Not Found!"
# print(update_pet_age(pet_info, "Spot", 26))
    
# LIST COMPREHENSIONS => []
# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

# print(pet_info)

# new_pet_list = [pet.get("name").upper() for pet in pet_info]

# print(new_pet_list)

# find like
#41. ✅ Use list comprehension to find a pet named spot
# spot =  [RETURNED PET / LOOP / CONDITIONAL]
# spot = [pet for pet in pet_info if pet.get("name") == "Spot" ]
# print(spot)

# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old

# young_pets =  [RETURNED PET / LOOP / CONDITIONAL]

# young_pets = [pet for pet in pet_info if pet.get("age") < 12]
# print(young_pets)

# GENERATOR EXPRESSION => ()
#43. ✅ Create a generator expression matching the filter above

#MAIN BENEFIT => LESS MEMORY INTENSICE


# young_pets = (pet for pet in pet_info if pet.get("age") < 12)
# print(young_pets)
