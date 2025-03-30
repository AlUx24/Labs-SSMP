import random


U = set(range(1, 26))


U_list = list(U)


A = set(random.sample(U_list, 12))
B = set(random.sample(U_list, 14))
C = set(random.sample(U_list, 9))


not_A_and_B = U - (A & B)
not_A = U - A
not_C = U - C

result = not_A_and_B - (not_A & not_C)


print("Універсальна множина U:", sorted(U))
print("Множина A:", sorted(A))
print("Множина B:", sorted(B))
print("Множина C:", sorted(C))
print("Результат:", sorted(result))
print("Потужність результату:", len(result))
