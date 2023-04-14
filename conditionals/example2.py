# Learning Conditonals with Input

name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)

if age < 18:
    print('You are too young '+name)
else:
    print('Welcome onboard '+name)

# CLASS EXERCISE
#Q1:
# Write a program that takes a number as input 
# from the user and prints "Positive" if the 
# number is greater than zero, "Negative" if 
# the number is less than zero, and "Zero" if 
# the number is equal to zero.
#Q2:
# Write a program that takes two numbers 
# as input from the user and prints the larger number.
#Q3: 
# Write a program that takes a string as input 
# from the user and checks if the string starts 
# with the letter "a". If it does, print "Starts with 'a'", 
# otherwise print "Does not start with 'a'".
#Q4:
# Write a program that takes a number as input 
# from the user and checks if the number is even or odd. 
# If it is even, print "Even", otherwise print "Odd".
# Q5:
# Write a program that takes a grade as 
# input from the user (e.g. "A", "B", "C", "D", "F") 
# and prints "Pass" if the grade is "A", "B", or "C", 
# and "Fail" if the grade is "D" or "F".