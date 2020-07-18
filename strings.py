name = 'Daniel'
age = 37

# Concatenate
print('Hello ' + name)
print('Hello ' + name + ' ddd ' + str(age))

# String formating
# Arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
# print('{age}, {name}'.format(name=a, age=b))

#F SRINGS
print(f'My name {name}')

#String methods

s = 'hello there world'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))