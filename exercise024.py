# My answer
userInput = ''


def isVowel(inputLetter):
    vowelList = ['a', 'e', 'i', 'o', 'u']
    result = False
    for letter in vowelList:
        if inputLetter.lower() == letter:
            result = True
            break
        else:
            continue
    return result


while len(userInput) == 0 or len(userInput) > 1:
    userInput = input('Type a single letter: ')

print(f'\nThe letter "{userInput}" is a vowel?\nAnswer: {isVowel(userInput)}')

print()

# Solution


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


print(is_vowel('c'))
print(is_vowel('e'))
