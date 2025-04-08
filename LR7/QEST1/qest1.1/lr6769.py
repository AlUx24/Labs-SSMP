# Створюємо файл input.txt з вмістом
with open("input.txt", "w") as infile:
    infile.write("Three\n")
    infile.write("Thirty eight\n")
    infile.write("Seven\n")
    infile.write("Six\n")
    infile.write("Thirty three\n")

# Зчитування рядків з input.txt
with open("input.txt", "r") as infile:
    lines = [line.rstrip('\n') for line in infile]

# Знаходимо максимальну довжину рядків
max_len = max(len(line) for line in lines)

# Відбираємо тільки найдовші рядки
longest_lines = [line for line in lines if len(line) == max_len]

# Записуємо ці рядки в output.txt
with open("output.txt", "w") as outfile:
    for line in longest_lines:
        outfile.write(line + "\n")

print("Готово! Файли input.txt і output.txt створені.")
