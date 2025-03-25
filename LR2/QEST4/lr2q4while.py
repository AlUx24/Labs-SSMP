a = 36
b = 60

x = a
y = b
while y != 0:
    x, y = y, x % y

print(f"НСД (while): {x}")

# Вхідні дані:
# a = 36
# b = 60
#
# Вихідні дані:
# НСД (while): 12
