import random

array = [random.randint(-50, 50) for _ in range(21)]
print("Масив:", array)

positive_count = 0
product = 1
for num in array:
    if num > 0:
        positive_count += 1
        if positive_count in [2, 4, 6]:
            product *= num
print("Добуток 2-го, 4-го, 6-го додатного елемента:", product)