# My answer
originalString = input('Type something: ')
numCopies = int(input('How many copies you want? (Max 10): '))

if originalString and numCopies <= 10:
    print(('\n'+originalString) * numCopies)

print()

# Solution


def larger_string(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result


print(larger_string('abc', 2))
print(larger_string('.py', 3))
