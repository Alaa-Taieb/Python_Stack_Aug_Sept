# Given a number as parameter, return true if it's Prime, false if it's not.
# A prime number is a number that is only divisible by 1 and itself.

# 17 => x * 2 => 17

def is_prime(number):
    if number <= 1:
        return False
    test = True
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            test = False
    return test

def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i < int(number/2)+1:
        if number % i == 0:
            return False
        i += 1
    return True


print(is_prime(3))
print(is_prime(5))
print(is_prime(7))
print(is_prime(11))
print(is_prime(13))
print(is_prime(17))
print(is_prime(35))

print(is_prime(8))
print(is_prime(6))
print(is_prime(4))

# Define a method that given a parameter x, will return a list containing the first x prime numbers.

def XPrime(x):
    new_list = []
    i = 2
    while x != 0:
        if is_prime(i):
            x -= 1
            new_list.append(i)
        i += 1
    return new_list

print(XPrime(10))
