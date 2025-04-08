def F3(string):
    count = 0
    for ch in string:
        code = ord(ch)
        # Англійські літери: великі (65–90), малі (97–122)
        if not ((65 <= code <= 90) or (97 <= code <= 122)):
            count += 1
    return count

# Тестування
test_string = "Hello, World! 123 :)"
result = F3(test_string)
print(f"Кількість неалфавітних символів у рядку: {result}")

# Вхідні дані:
# "Hello, World! 123 :)"
# Вихідні дані:
# Кількість неалфавітних символів у рядку: 10
