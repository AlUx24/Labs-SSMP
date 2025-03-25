a = 36
b = 60
min_num = min(a, b)
gcd = 1

for i in range(1, min_num + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(f"НСД (for): {gcd}")

# Вхідні дані:
# a = 36
# b = 60
#
# Вихідні дані:
# НСД (for): 12
