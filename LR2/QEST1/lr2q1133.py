a = int(input())
b = int(input())
c = int(input())
s = int(input())

if s <= a:
    tax = 0
elif a < s <= b:
    tax = s * 0.10
elif b < s <= c:
    tax = s * 0.25
else:
    tax = s * 0.50

print(tax)

# Вхідні дані:
# 1000
# 500
# 700
# 3200
#
# Вихідні дані:
# 1600.0
