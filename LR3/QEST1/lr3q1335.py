test_cases = ["3+3=6", "2 * 3 = 6"]

for s in test_cases:
    digits = ''.join([ch for ch in s if ch.isdigit()])
    print(digits)

# Вхідні дані:
# 3+3=6
# 2 * 3 = 6
#
# Вихідні дані:
# 336
# 236
