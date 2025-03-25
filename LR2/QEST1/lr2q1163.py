shape = input()

if shape == "triangle":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(area)

elif shape == "rectangle":
    a = float(input())
    b = float(input())
    print(a * b)

elif shape == "circle":
    r = float(input())
    print(3.14 * r * r)

# Вхідні дані:
# triangle
# 3
# 4
# 5
#
# Вихідні дані:
# 6.0
