test_cases = [
    [1, 2, 1],
    [1, 3, 2, 4, 2],
    [1, 2, 3]
]

for lst in test_cases:
    count = 0
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            count += 1
    print(count)

# Вхідні дані:
# 1 2 1
# 1 3 2 4 2
# 1 2 3
#
# Вихідні дані:
# 1
# 2
# 0
