# Створення файлу numbers.txt з 10 числами
with open("numbers.txt", "w") as f:
    for num in [5, 12, 7, 3, 9, 6, 1, 4, 8, 10]:
        f.write(str(num) + "\n")

# Зчитування та обчислення суми
with open("numbers.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]

total = sum(numbers)
print("Сума чисел:", total)

# Запис суми у файл sum_numbers.txt
with open("sum_numbers.txt", "w") as f:
    f.write(str(total))
