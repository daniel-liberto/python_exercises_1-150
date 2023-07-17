# My answer
inputList = []
concatList = ''

print('Type 3 random words')
while len(inputList) < 3:
    inputList.append(input(f'Word number {len(inputList) + 1}: '))

for item in inputList:
    concatList += item

print(f'\n Concatenating your 3 words, the result is: "{concatList}"')

print()

# Solution


def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
    return result


print(concatenate_list_data([1, 5, 12, 2]))
