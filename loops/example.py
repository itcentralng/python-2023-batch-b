# For Loop

for char in "ZAINAB":
    print(char)

print('--------------------')
print('| FRUIT    | TASTE |')
print('--------------------')
for fruit in ['Coconut', 'Apple', 'Orange']:
    if fruit == 'Orange':
        print("| "+fruit+"   | Sour  |")
    elif fruit == 'Apple':
        print("| "+fruit+"    | Sweet |")
    else:
        print("| "+fruit+"  | Sweet |")
print('--------------------')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print([number for number in numbers if number%2==0])
print([number for number in numbers if number%2>0])
print([fruit for fruit in ['Orange', 'Cashew', 'Guava', 'Apple'] if fruit.startswith('O') == False])

for number in numbers:
    if number % 2 == 0:
        print(number)

for number in numbers:
    if number % 2 > 0:
        print(number)

# While Loop


counter = 0
while counter < len(numbers):
    print(numbers[counter])
    counter += 1