cartels = {
    'escobar': 'Medellin',
    'gustavo': 'Medellin',
    'pacho': 'Cali',
}

print('The cartel of Pablo Escobar is', cartels['escobar'])
print('The cartel of Pacho is', cartels['pacho'])
print('The cartel of Gustavo is', cartels['gustavo'])

# History spoiler
print('Gustavo was killed')
cartels['gustavo'] = 'The Hell'

print('The cartel of Gustavo is', cartels['gustavo'])


cartels['miguel'] = 'Cali'
print('The cartel of Miguel is', cartels['miguel'])
