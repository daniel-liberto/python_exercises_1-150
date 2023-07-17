# My answer
userNumber = int(input('Type a integer number: '))
if userNumber % 2:
    print(f'The number "{userNumber}" is odd.')
else:
    print(f'The number "{userNumber}" is even.')

print()

# Solution
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
