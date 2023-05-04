"""
1. Write a fuction that returns the first two integers from
    a list of integers. Using list slicing, get the new numbers
    in reverse.

2. Write a function that takes two names and retun them as
    one seperated by space. Using the right string method,
    check if the first name starts with upper case.
"""

# Answer
# 1.
def get_first_two_integers(list_of_integers):
    return list_of_integers[:2]

first_two = get_first_two_integers([1, 2, 3, 4, 5])
print(first_two)

numbers_in_reverse = first_two[::-1]
print(numbers_in_reverse)

def merge_names(first_name, second_name):
    return '{} {}'.format(first_name, second_name)

my_names = merge_names('Musty','Ahmad')
print(my_names)
print('First Name Starts With Capital Letter: ', my_names[0].isupper())

"""
3. Write a function that takes a number and return for example:
    '2 is an even number' if 2 were to be passed to the function or
    '3 is an odd numebr' if 3 were to be passed to the function.
"""