s = "abcdefg"  

half = (len(s) + 1) // 2  
result = s[half:] + s[:half]

print(result)

# Вхідні дані:
# abcdefg
#
# Вихідні дані:
# efgabcd