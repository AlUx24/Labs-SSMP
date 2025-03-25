cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kiev', 'Hong Kong']

result = ', '.join(cities[:-1]) + ' and ' + cities[-1]
print(result)

longest = max(cities, key=len)
print("Найдовша назва міста:", longest)

# Вхідні дані:
# ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kiev', 'Hong Kong']
# Вихідні дані:
# Budapest, Rome, Istanbul, Sydney, Kiev and Hong Kong
# Найдовша назва міста: Hong Kong