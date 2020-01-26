# Playing with basic data types

# --- Integers and Floats --- #
numInt = 3
print(type(numInt))

numFloat = 3.456
print('type(numFloat)=', type(numFloat), '\n')
print("-----------------------------------------------------------------------")

print('abs(10.15)={}{}'.format(abs(10.15), '\n'))
print("-----------------------------------------------------------------------")

print('round(3.75)={}{}'.format(round(3.75), '\n'))
print('round(3.75, 1)={}{}'.format(round(3.75, 1), '\n'))
print("-----------------------------------------------------------------------")

num_1 = int('100')
num_2 = int('200')
print(f'num_1 + num_2 = {(num_1 + num_2)}')
print("-----------------------------------------------------------------------")

# --- Strings --- #
greeting = 'hello world!'
print(greeting, '\n')
print(dir(greeting), '\n')
print('var greeting capitalized={}'.format(greeting.capitalize()), '\n')
print('var greeting uppercase={}'.format(greeting.upper()))

print(help(str))

print(help(str.lower))

