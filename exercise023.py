# My answer
userInput = input('Type a word: ')
copies = int(input('How many copies do you want? '))

if len(userInput) <= 2:
    print(f'The result is: {userInput * copies}')
else:
    print(f'The result is: {userInput[0:2] * copies}')

print()

# Solution


def substring_copy(text, n):
    flen = 2
    if flen > len(text):
        flen = len(text)
    substr = text[:flen]
    result = ""
    for i in range(n):
        result = result + substr
    return result


print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))
