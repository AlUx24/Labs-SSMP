def reverse_number(n, result=0):
    if n == 0:
        return result
    else:
        return reverse_number(n // 10, result * 10 + n % 10)

def main():
    try:
        num = int(input("Введіть ціле число: "))
        reversed_num = reverse_number(num)
        print(f"Число-перевертень: {reversed_num}")
    except ValueError:
        print("Помилка: потрібно ввести ціле число!")

# Тестування
if __name__ == "__main__":
    main()

# Вхідні данні:
# 1234
# Вихідні данні:
# 4321