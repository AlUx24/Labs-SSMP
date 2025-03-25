test_cases = ["Ada", "Able was I ere I saw Elba", "10501", "Origin"]

for line in test_cases:
    cleaned = ''.join(line.lower().split())
    print(cleaned == cleaned[::-1])

# Вхідні дані:
# Ada
# Able was I ere I saw Elba
# 10501
# Origin
#
# Вихідні дані:
# True
# True
# True
# False
