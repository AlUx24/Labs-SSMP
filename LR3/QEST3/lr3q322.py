s = "abcdefgh"
half = (len(s) + 1) // 2
result = s[half:] + s[:half]
print(result)

# Вхідні дані:
# abcdefgh
#
# Вихідні дані:
# efghabcd