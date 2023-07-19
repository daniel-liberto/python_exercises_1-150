# My answer
inputOne = input('type a word or number (1): ')
inputTwo = input('type a word or number (2): ')


class Object:
    def __init__(self, value):
        self.value = value
        print(f'This is a object with a value of: {self.value}')
        print(f'Type: {type(self)}\n')


if inputOne.isdigit() and inputTwo.isdigit():
    inputOne = int(inputOne)
    inputTwo = int(inputTwo)
    print()
    objectOne = Object(inputOne)
    objectTwo = Object(inputTwo)
else:
    print(f'\nThis is the first input you used it: "{inputOne}"')
    print(f'Type: {type(int(inputOne) if inputOne.isdigit() else inputOne)}')
    print(f'\nThis is the second input you used it: "{inputTwo}"')
    print(f'Type: {type(int(inputTwo) if inputTwo.isdigit() else inputTwo)}')

print()

# Solution


def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be integers!"
    return a + b


print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))
