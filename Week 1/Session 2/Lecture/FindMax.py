# Given a list as an input, return the biggest value inside the list.

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


# my_list = [5,16,22,4,-5,39,99,0]
# max = find_max(my_list)
# print(max)

print(find_max([5,16,22,4,-5,39,99,0]))