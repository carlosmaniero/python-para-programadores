# Create a fruits lists
fruits = ['banana', 'apple']

print('Size of fruits:', len(fruits))
print('Minions loves', fruits[0])
print('Newton loves', fruits[1])

# Add new item to fruits list
fruits.append('orange')

print('Size of fruits:', len(fruits))
print(fruits[2], 'is the new black')

# Remove the first element
print('I don\'t like of', fruits.pop(0))
print('Now minions loves', fruits[0])
