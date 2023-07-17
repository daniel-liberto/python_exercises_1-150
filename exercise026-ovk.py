# My answer
userList = []


def showHistogram(data):
    for entity in data:
        entity = str(entity)
        # check if are less than 10, for a better representation
        print(f'{entity if len(entity) > 1 else f" {entity}"}: ' +
              '#' * int(entity))


def inputNumber(numList):
    numList = input(
        'Type integer numbers between 1 and 15 (ex: 1,6,7,2): ').split(',')

    for item in numList:
        item = item.strip()  # if someone put whitespaces
        if item.isdigit():
            item = int(item)
            if item == 0 or item > 15:
                print('ERROR: must be a number between 1 and 15.')
                break
            else:
                userList.append(item)
        else:
            print(f'\n"{item}" is a WRONG NUMBER, type a valid number.\n')


while len(userList) == 0:
    inputNumber(userList)


print('\n------Histogram------')
print('Num      Chart')
showHistogram(userList)
print('---------------------')

print()

# Solution


def histogram(items):
    for n in items:
        output = ''
        times = n
        while (times > 0):
            output += '*'
            times = times - 1
        print(output)


histogram([2, 3, 6, 5])
