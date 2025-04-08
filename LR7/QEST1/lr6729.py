import math

# Тестові вхідні дані
numbers = [7.9, 5.8]

for n in numbers:
    result = math.modf(n)
    print(result)

# Вхідні дані:
# 7.9
# 5.8
#
# Вихідні дані:
# (0.9000000000000004, 7.0)
# (0.7999999999999998, 5.0)
