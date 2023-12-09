# Integer Pointer
num1 = 11
num2 = num1
print('\nBefore Changed num2')
print('num1 = ',num1)
print('num2 = ',num2)
print('num1 point to ',id(num1))
print('num2 point to ',id(num2))

num2 = 22

print('\nAfter Changed num2')
print('num1 = ',num1)
print('num2 = ',num2)
print('num1 point to ',id(num1))
print('num2 point to ',id(num2))

# Dictionary Pointer
dict1 = {'value':11}
dict2 = dict1
print('\nBefore Changed dict2')
print('dict1 = ',dict1)
print('dict2 = ',dict2)
print('dict1 point to ',id(dict1))
print('dict2 point to ',id(dict2))

dict2['value']= 20

print('\nAfter Changed dict2')
print('dict1 = ',dict1)
print('dict2 = ',dict2)
print('dict1 point to ',id(dict1))
print('dict2 point to ',id(dict2))

dict3 = {'value':30}
dict2 = dict3

print('\nAfter creating dict3')
print('dict1 = ',dict1)
print('dict2 = ',dict2)
print('dict3 = ',dict3)
print('dict1 point to ',id(dict1))
print('dict2 point to ',id(dict2))
print('dict3 point to ',id(dict3))



