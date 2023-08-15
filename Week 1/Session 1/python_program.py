
print("Hello World!")

# Variables 

# Numbers
my_integer = 15 
my_second_integer = 30
my_float = 15.5

my_final_integer = my_integer + my_second_integer


print(f"my_final_integer = {my_final_integer}")

# String 
my_string = "This is part one of the string,"
my_second_string = " and this is the second part of it!"

# Concatenation
my_final_string = my_string + my_second_string

print(my_final_string)

# Boolean
my_boolean = True
print(my_boolean)

# Lists

my_list = [0 , 1 , "Third Item" , 3]
print(f"my_list = {my_list}")
my_list[2] = "THIRDDDDD"
print(my_list[2])

# Dictionaries
# key-value pairs
# Unordered
# Mutable
# Indexed by KEY

# Creating a dictionary
my_dictionary = {
    # [KEY]             [VALUE]
    'Stack Name': "Python Web Development",
    'Duration': "2 Months",
    'Instructor': "Alaa Taieb",
    'Student Count': 41,
    'Course Status': True
}

print(f"Student Count: {my_dictionary['Student Count']}")
# x += 1 => x = x + 1
my_dictionary['Student Count'] += 1
print(f"Student Count: {my_dictionary['Student Count']}")

# Tuples
# Initialize a tuple

my_tuple = (0 , 1 , "Third Item" , 3)
print(f"my_tuple: {my_tuple}")
print(my_tuple[2])

# Casting or Converting
new_list = list(my_tuple)
new_list[2] = "FORCED TO BE MUTABLE"
my_tuple = tuple(new_list)
print(my_tuple)
# WE CAN NOT CHANGE ITS VALUE

# Multiple Assignments and unpacking
coordinates = (25.1255, 30.005)
latitude = coordinates[0]
longitude = coordinates[1]


latitude , longitude = coordinates

print(f"Coordinates = [{latitude},{longitude}]")

# Conditionals

is_hungry = True
is_fit = False
if not is_hungry:
    print("Workout")
elif is_fit:
    print("EAT")
else: 
    print("Workout")

# Loops

# For loop
for i in range(5):
    print(i)

# Length of a list is calculated using the len() method
# len() => number (int)
print("*"*50)

print(len(my_list))

print("*"*50)
for i in range(len(my_list)):
    print(my_list[i])
print("*"*50)

for item in my_list:
    print(item)

# Methods | Functions
def greet(name="Everyone"):
    print(f"Hello {name}!")



greet("Emna")

def add(x , y):
    return x + y

sum = add(5,7) # 12
sum = add(sum , 3) # 15
print(sum)