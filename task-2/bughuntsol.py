def calc_average(numbers):
    total = 0
    count = 0                                                                                # == is not correct assign operator while = is
    for num in numbers:
        total += num
        count += 1 
    avg = total / count                                                                      # There is no coun variable it should be mentioned as count
    return avg

# Test the function
nums = [10, 20, 30, 40, 50]
result = calc_average(nums)
print("Average:", result)                                                                   # There is no resul variable it should be mentioned as result
# Check if the average is even or odd
if result % 2 == 0:                                                                         # = is not correct comparision operator while == is
    print("The average is even")
else:
    print("The average is odd")

# Generate a list of squares
squares = [num ** 2 for num in nums]                                                        # '[' is not closed, so use ']' to close 
print("Squares:", squares)

# Find the maximum square
max_square = max(squares)
print("Maximum square:", max_square)                                                        # There is no max_squar variable it should be mentioned as max_square

# Search for a specific square
target_square = 900
if target_square in squares:                                                                 # ':' must be used for correct indentation 
    print("Target square found at index:", squares.index(target_square))  
else:
    print("Target square not found")

# Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined list:", combined_list)

# Remove duplicates from the list
unique_list = list(set(combined_list))  
print("Unique list:", unique_list)

# Create a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Person's name:", person['name'])
print("Person's gender:", person.get('gender', 'Unknown'))  

# Update the person's age
person['age'] = 26
print("Updated age:", person['age'])                                                           # '[' is not closed, so use ']' to close 

# Add a new key-value pair
person['job'] = 'Engineer'

# Delete the city key
del person['city']                                                                             # keys must be in string from 

# Print all key-value pairs in the dictionary
for key, value in person.items():                                                             # items() is the correct way to call the inbuilt function
    print(key + ': ' + str(value))                                                            # convert the value into string to concatnate it
    
# Check if person is from London
if 'city' in person.keys():                                                                   # check whether the key city is present in the dictionary person or not
    if person['city'] == 'London':                                                            # = is not correct comparision operator while == is
        print("Person is from London")
    else:
        print("City is not found!")

# Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:                                                                                     # ':' must be used for correct indentation 
        return n * factorial(n-1)  

print("Factorial of 5:", factorial(5))

# Create a list of numbers
numbers = range(10)
print("Numbers:", numbers) 

# Print each number in the list
for num in numbers:                                                                           # ':' must be used for correct indentation 
    print(num)  

# Define a class for a car
class Car:                                                                                    # ':' must be used for correct indentation 
    global self                                                                               # global self must be assigned as the word self is also used in another function
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):                                                                            # parameter must be given
        print("Car:", self.make, self.model)                                                   # use the correct variables 

my_car = Car("Toyota", "Corolla")
my_car.info()

# Access class attributes directly
print("Car make:", my_car.make)
print("Car model:", my_car.model)

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
#my_tuple[0] = 10                                                                             #tuple are immutable

# Open a file for writing
file = open('my_file.txt', 'w')
file.write("Hello, world!")                                                                   # '(' is not closed, so use ')' to close 

# Close the file
file.close 

# Find the length of a string
message = "Hello, world!"
length = len(message)                                                                        # length must be in int not in str

# Convert a string to uppercase
uppercase_message = message.upper()                                                          # upper() is the correct way to call the inbuilt function
print("Uppercase message:", uppercase_message)

# Split a sentence into words
sentence = "This is a sentence"
words = sentence.split()                                                                     # there is not ',' in the sentence so cant split, thus dont give any parameter to split the words
print("Words:", words)

# Define a function to calculate the power of a number
def power(base, exponent):
    result = base ** exponent
    return result

# Calculate the power of 2 to the 3
print("2^3:", power(2, 3))

# Use a list as a stack
stack = []
stack.append(1)                                                                             # push is not a inbuilt function and also has not been declared earlier by user in this program, so use append
stack.append(2)
stack.append(3)
print("Stack:", stack)

# Pop elements from the stack
print(stack.pop())
print(stack.pop())

# Attempt to pop from an empty stack
print(stack.pop())

# Use a dictionary as a switch-case
def switch_case(case):
    cases = {
        'a': "Case a",
        'b': "Case b",
        'c': "Case c",
    }
    return cases.get(case, "Invalid case")                                               # return invalid case warning

print(switch_case('b'))
print(switch_case('d'))  

# Open and read a file
file = open('data.txt', 'w+')                                                            # open in w+ mode as the file is not already present in the system
content = file.read()
print("File content:", content)

# Close the file
file.close()

# Attempt to read from a closed file
if file is open:
    print(file.read())                                                                   # use if statement to check whether the file is close or open 
else:
    print("File is closed. open again to read !")

# Perform division
numerator = 10
denominator = 0
if denominator != 0:                                                                     # check if its not 0  
    result = numerator / denominator                                                     # There is no denominaotr variable it should be mentioned as denominator

# Print the result
print("Result:", result)

# Use a while loop to count from 1 to 5
count = 1
while count <= 5:                                                                        # ':' must be used for correct indentation 
    print(count)
    count += 1

# Print the sum of the numbers from 1 to 10
sum = 0
for i in range(11):
    sum += 1

print("Sum:", sum)

# Access elements of a list using an invalid index
my_list = [1, 2, 3, 4, 5]
try:
    print(my_list[10])                                                                  # the index 10 is wrong , since the max is 4, thus use try-except to display th error 
except IndexError as e:
    print("An IndexError occurred:", e)

# Define a function that takes a default argument
def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Alice")

# Swap two variables
a = 5
b = 10
a, b = b, a  

# Use an invalid escape sequence in a string
invalid_string = 'This is an \\q invalid escape sequence'

# Print the invalid string
print(invalid_string)

# Use an invalid operator
x = 10
y = 3
result = x // y  

# Print the result
print("Result:", result)
