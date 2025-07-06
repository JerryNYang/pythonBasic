import math
# Using math functions 
print(math.sqrt(25)) # Output: 5.0 
print(math.pow(2, 3)) # Output: 8.0 
print(math.sin(math.pi/2)) # Output: 1.0 

# Using math operators 
x = 10 y = 3 print(x + y) # Output: 13 
print(x / y) # Output: 3.3333333333333335 
print(x // y) # Output: 3 
print(x % y) # Output: 1 
print(x ** y) # Output: 1000 

age = input("Enter your age: ")
age = int(age)  # Convert the input to an integer


print("You will be " + str(age + 1) + " next year.")

# Built-in method example
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
print("Length:", length)


# User-defined method example
def greet(name):
    print("Hello, " + name)


greet("Alice")
