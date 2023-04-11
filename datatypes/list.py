people = ['Aisha', 'Ibrahim', 'Zainab', 'Mustapha']

shopping = []

# print(people)

people.append('Musa')
# print(people)

numbers = [1, 2, 3]
print(numbers)
numbers.append(4)
numbers.append(5)
numbers.append(6)
print(numbers)
numbers.clear()
print(numbers)

textbooks = ["Maths", "English"]
notebooks = textbooks.copy()

print(textbooks)
print(notebooks)

alphabets = ['a', 'b', 'c', 'd', 'a', 'b']

print(alphabets.count('a'))
print(alphabets.count('c'))

f = ['cashew', 'pawpaw']
fruits = ["apple", "orange"]
fruits.append('banana')
fruits.extend(f)
print(fruits)

print(fruits[::2])
print(fruits[::-1])