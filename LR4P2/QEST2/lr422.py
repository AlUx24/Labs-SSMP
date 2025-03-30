numbers = "1 2 3 2 3 4 5 1 6".split()
seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)

# Вхідні дані:
# 1 2 3 2 3 4 5 1 6

# Вихідні дані:
# NO
# NO
# NO
# YES
# YES
# NO
# NO
# YES
# NO