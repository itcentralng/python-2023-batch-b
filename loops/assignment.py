""" 
Q1: 
Print integers 1-to-15, 
but print “Fizz” if an integer is divisible by 3, 
“Buzz” if an integer is divisible by 5, 
and “FizzBuzz” if an integer is divisible 
by both 3 and 5.
"""

# for i in range(1, 16):
#     if i % 5 == 0 and i % 3 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


i = 1

while i < 16:
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    i+=1