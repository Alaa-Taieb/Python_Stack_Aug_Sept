from datetime import datetime
import time
# Define a method that [RECURSIVELY] calculates the factorial of parameter n.

# A recursive method is a method that achieves a certain task without using loops but with calling itself.



def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)



# Define a method that  calculates the factorial of parameter n.

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f


start = time.time()
# time_before_f1 = datetime.now()
print(fact(100))
end = time.time()
print(f"with loops = {end - start}")
# time_after_f1 = datetime.now()
start = time.time()

print(factorial(100))
end = time.time()
print(f"with rec = {end - start}")
# time_after_f2 = datetime.now()

# t2 = datetime.timestamp(time_after_f2) - datetime.timestamp(time_after_f1)
# t1 = datetime.timestamp(time_after_f1) - datetime.timestamp(time_before_f1)



# print(f"Factorial with loop took {t1} milliseconds.")
# print(f"Factorial with recessivity took {t2} milliseconds.")