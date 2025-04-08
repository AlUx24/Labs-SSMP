from datetime import date

class Student:
    def __init__(self, id, last_name, first_name, middle_name, birth_date, address,
                 phone, faculty, course, group):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birth_date = birth_date  # формат: 'YYYY-MM-DD'
        self.address = address
        self.phone = phone
        self.faculty = faculty
        self.course = course
        self.group = group

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.faculty}, курс {self.course}, група {self.group})"

    def get_birth_year(self):
        return int(self.birth_date.split("-")[0])

# Створення списку студентів
students = [
    Student(1, "Іваненко", "Олег", "Петрович", "2002-03-15", "Рівне", "123456", "ФІТ", 2, "ІП-21"),
    Student(2, "Петренко", "Марія", "Іванівна", "2001-06-12", "Луцьк", "654321", "ФМЕ", 3, "ЕП-31"),
    Student(3, "Сидоренко", "Андрій", "Михайлович", "2003-11-01", "Львів", "789456", "ФІТ", 1, "ІП-11"),
    Student(4, "Коваленко", "Оксана", "Віталіївна", "2000-02-25", "Київ", "111222", "ФІТ", 4, "ІП-41"),
]

# 1. Студенти заданого факультету
faculty = "ФІТ"
print(f"\nСтуденти факультету {faculty}:")
for s in students:
    if s.faculty == faculty:
        print(s)

# 2. Списки студентів для кожного факультету та курсу
print("\nСписки студентів за факультетами та курсами:")
grouped = {}
for s in students:
    key = (s.faculty, s.course)
    grouped.setdefault(key, []).append(s)

for (fac, crs), group in grouped.items():
    print(f"{fac}, курс {crs}:")
    for s in group:
        print("  ", s)

# 3. Студенти, які народились після заданого року
year = 2001
print(f"\nСтуденти, народжені після {year}:")
for s in students:
    if s.get_birth_year() > year:
        print(s)

# 4. Студенти певної навчальної групи
group_name = "ІП-21"
print(f"\nСтуденти групи {group_name}:")
for s in students:
    if s.group == group_name:
        print(s)
