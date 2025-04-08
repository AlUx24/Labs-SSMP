import csv
import os
import glob

# 1. Створення файлу painters.csv
with open("painters.csv", "w", encoding="utf-8") as f:
    f.write("author,canvas\n")
    f.write('Vincent Willem van Gogh,"Vase with sunflowers"\n')
    f.write('Rembrandt Harmenszoon van Rijn,"Aristotle"\n')
    f.write('Leonardo da Vinci,"Self-portrait"\n')

# 2. Зчитування painters.csv через DictReader
with open("painters.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    painters = list(reader)

print("Зміст painters.csv:")
for painter in painters:
    print(painter)

# 3. Створення imdb.csv зі списку словників
imdb = [
    {'title': 'Lord of the Rings: Two towers', 'year': 2002, 'rating': 8.7},
    {'title': 'Matrix', 'year': 1999, 'rating': 8.7},
    {'title': 'Interstellar', 'year': 2014, 'rating': 8.5},
    {'title': 'Back to the Future', 'year': 1985, 'rating': 8.5},
    {'title': 'Logan: Wolverine', 'year': 2017, 'rating': 8.1}
]

with open("imdb.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "year", "rating"])
    writer.writeheader()
    writer.writerows(imdb)

print("\nФайл imdb.csv створено.")

# 4. Поточний каталог і список файлів
print("\nПоточний каталог:", os.getcwd())
print("Список файлів:")
for file in os.listdir():
    print("-", file)

# 5. Розмір файлу painters.csv
file_to_check = "painters.csv"
if os.path.exists(file_to_check):
    size = os.path.getsize(file_to_check)
    print(f"\nРозмір файлу '{file_to_check}': {size} байтів")
else:
    print(f"\nФайл '{file_to_check}' не знайдено.")

# 6. Пошук усіх CSV-файлів у каталозі
print("\nФайли *.csv у поточному каталозі:")
csv_files = glob.glob("*.csv")
for file in csv_files:
    print("-", file)
