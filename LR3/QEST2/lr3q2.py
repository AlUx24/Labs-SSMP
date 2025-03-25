s = "Python is awesome!"

print(s[2])           # третій символ
print(s[-2])          # передостанній символ
print(s[:5])          # перші 5 символів
print(s[:-2])         # весь рядок, крім останніх двох символів
print(s[::2])         # символи з парними індексами
print(s[1::2])        # символи з непарними індексами
print(s[::-1])        # всі символи в зворотному порядку
print(s[::-2])        # всі символи через один в зворотному порядку
print(len(s))         # довжина рядка

# Вхідні дані:
# Python is awesome!
#
# Вихідні дані:
# t
# e
# Pytho
# Python is awesom
# Pto saeo!
# yhniswsm
# !emosewa si nohtyP
# !eoa inotP
# 18