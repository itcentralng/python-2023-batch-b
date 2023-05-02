def sum5and6():
    print(5+6)

def specialprint(whattoprint):
    print('Special: ', whattoprint)

def sumnumbers(num1, num2, num3):
    print(num1+num2+num3)

def sumanother(num1=5, num2=6):
    print(num1+num2)

def getEven(numbers):
    return [number for number in numbers if number % 2 == 0]

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evennums = getEven(x)

def getDouble(numbers):
    return [number*2 for number in numbers]

print(getDouble(evennums))