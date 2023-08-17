# Default Values in functions

def greet(name="Everyone"):
    print(f"Hello {name}!")

greet("Saber")

# Parameter order in functions 

def add(a , b):
    print(f"a = {a} | b = {b} | a + b = {a + b}")

add(b=5 , a=6)

# Ignoring the missing code block error.

def CalculateSomething():
    pass

if True:
    pass


CalculateSomething()
CalculateSomething()
CalculateSomething()