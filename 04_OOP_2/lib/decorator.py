# 1. ✅ First Class Functions
# "[We can] assign them to variables, store them in data structures, pass them as arguments
# to other functions, and even return them as values from other functions."
# See more => http://bit.ly/3YQh8KR

    # Create functions to be used as callbacks 

#First Class functions

# def walk(pet):
#     print(f'{pet} has been walked!')

# def feed(pet):
#     print(f'{pet} had been fed!')


    # Create a higher-order function that will take a callback as an argument
#Higher order function => accepts a function
# def execute_task(func):

#     #Callback function Invocation
#     return func("Rose")


# execute_task(walk)
# execute_task(feed)

# 2. ✅ Create a higher-order function that returns a function

# def execute_task():
#     def feed (pet):
#         print(f'{pet} has been fed!')
    
#     return feed

# print(execute_task()) # returns the feed funciton reference

#if we end with a fucntion reference then we can run this code below
# execute_task()("Rose")

# 3. ✅ Decorator

# Create a function that:
    # - takes a function as an argument
    # - has an inner function defined 
    # - returns the inner function

# Tools:

    # .format() => Method (String)
    # https://www.geeksforgeeks.org/python-string-format-method/

    # .round() => Format Actual Calclation of Discount
    # https://www.geeksforgeeks.org/round-function-python/

#Decorator
def coupon_calculator(func):

    #Inner Function
    def report_price():
        print(f'Initioal Price = $35.00')
        final_price = func(35.00)
        print(f'Newly Discounted Price = ${final_price}')

    return report_price


#Callback function to calculate new price
# def calculate_price(price):

#     # we end up with a floating point number rounded to the newarest hundreth
#     return '{:.2f}'.format(round( price / 2, 2))

# report_price = coupon_calculator(calculate_price)
# report_price()

# Try using a decorator with / without pie syntax '@'

# Without pie syntax 

# With pie syntax

@coupon_calculator
def calculate_price(price):

    # we end up with a floating point number rounded to the newarest hundreth
    return '{:.2f}'.format(round( price / 2, 2))


calculate_price()