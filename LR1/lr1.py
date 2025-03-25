import math

m = float(input("Введіть m: "))      # 2
c = float(input("Введіть c: "))      # -1
t = float(input("Введіть t: "))      # 1.2
b = float(input("Введіть b: "))      # 0.7

f = (m * math.tan(t) + abs(c * math.sin(t))) ** (1 / 3)
z = m * math.cos(b * t * math.sin(t)) + c

print("{:<20}".format(f"t = {t:.2f}").replace(' ', '#'))
print("{:<20}".format(f"f = {f:.5f}").replace(' ', '#'))
print("{:<20}".format(f"z = {z:.5f}").replace(' ', '#'))