# My answer
value = input('Enter numbers with comma between them(ex: 1,3,6,10): \n')
listValue = value.split(sep=',')
tupleValue = tuple(listValue)
print('List:', listValue)
print('Tuple:', tupleValue)

print()

# Solution
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)
