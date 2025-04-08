from datetime import date

# Вхідні дані
year1, month1, day1 = 2018, 8, 1
year2, month2, day2 = 2019, 3, 4

# Створення об'єктів дат
d1 = date(year1, month1, day1)
d2 = date(year2, month2, day2)

# Різниця між датами
delta = d2 - d1
print(delta.days)

# Вхідні дані:
# 2018 8 1
# 2019 3 4
#
# Вихідні дані:
# 215
