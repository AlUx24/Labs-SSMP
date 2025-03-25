nums = [2, 3, -6, 1]
total = 0
squares = 0
for num in nums:
    total += num
    squares += num ** 2
    if total == 0:
        break

print(squares)

# Вхідні дані:
# 2
# 3
# -6
# 1
#
# Вихідні дані:
# 50
