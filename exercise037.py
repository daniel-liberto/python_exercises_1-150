# My answer
name, age, address = '', 0, ''
person = {
    'name': input('Type your first name: '),
    'age': int(input('What is your age? ')),
    'address': input('Type your address: ')
}

print(
    '\nName:', person.get('name'),
    '\nAge:', person.get('age'),
    '\nAddress:', person.get('address'),
)

print()

# Solution


def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


personal_details()
