import os

# Створення файлу text1.txt
with open("text1.txt", "w", encoding="utf-8") as f:
    f.write("Це автоматично створений файл.\n")
    f.write("Він буде скопійований у text2.txt.\n")
    f.write("Потім text1.txt буде видалено.\n")

print("Файл text1.txt створено.")

# Копіювання вмісту у text2.txt
with open("text1.txt", "r", encoding="utf-8") as source, open("text2.txt", "w", encoding="utf-8") as target:
    content = source.read()
    target.write(content)

print("Вміст скопійовано у text2.txt.")

# Виведення вмісту text2.txt
with open("text2.txt", "r", encoding="utf-8") as f:
    copied_text = f.read()
    print("Вміст text2.txt:")
    print(copied_text)

# Видалення text1.txt
os.remove("text1.txt")
print("Файл text1.txt видалено.")
