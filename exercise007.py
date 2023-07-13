# My answer
filename = input('Enter a filename.extension: ')
nameFile = filename.split('.')[0]
extensionFile = filename.split('.')[1]
print('\nFilename is:', nameFile)
print('Extension is:', extensionFile)

print()

# Solution
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))
