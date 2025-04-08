def Inverse(n):
    sign = -1 if n < 0 else 1
    reversed_number = int(str(abs(n))[::-1])
    return sign * reversed_number

def main():
    total = 0
    print("Введіть 10 цілих чисел:")
    for _ in range(10):
        num = int(input())
        inv = Inverse(num)
        total += inv
    print("Сума обернених чисел:", total)

# Тестування функції
if __name__ == "__main__":
    main()
