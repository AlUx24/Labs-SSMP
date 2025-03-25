s = "Andromeda, M 31, NGC 224"

letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)

print(f"Letters {letters}")
print(f"Digits {digits}")

# Вхідні дані:
# Andromeda, M 31, NGC 224
#
# Вихідні дані:
# Letters 13
# Digits 5
