# My answer
originalString = input('Type a random word: ')
modifiedString = 'Is' + originalString

if originalString.startswith('Is'):
    print(
        f'\nYou type "{originalString}" and already starting with "Is", so it will be unchanged to "{originalString}".')
else:
    print(
        f'\nYou type "{originalString}" and is not starting with "Is", so it will be changed to "{modifiedString}"')

print()

# Solution


def new_string(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    return "Is" + text


print(new_string("Array"))
print(new_string("IsEmpty"))
