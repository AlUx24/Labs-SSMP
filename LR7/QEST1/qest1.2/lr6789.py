# Створення input.txt з прикладом
with open("input2.txt", "w") as f:
    f.write("DEPOSIT Sasha 100\n")
    f.write("INCOME 5\n")
    f.write("BALANCE Sasha\n")
    f.write("TRANSFER Sasha Elena 50\n")
    f.write("WITHDRAW Elena 100\n")
    f.write("BALANCE Elena\n")
    f.write("BALANCE Iryna\n")

# Логіка обробки команд
accounts = {}

with open("input2.txt", "r") as infile, open("output2.txt", "w") as outfile:
    for line in infile:
        parts = line.strip().split()
        command = parts[0]

        if command == "DEPOSIT":
            name, sum_ = parts[1], int(parts[2])
            accounts[name] = accounts.get(name, 0) + sum_

        elif command == "WITHDRAW":
            name, sum_ = parts[1], int(parts[2])
            accounts[name] = accounts.get(name, 0) - sum_

        elif command == "BALANCE":
            name = parts[1]
            if name in accounts:
                outfile.write(f"{accounts[name]}\n")
            else:
                outfile.write("ERROR\n")

        elif command == "TRANSFER":
            name1, name2, sum_ = parts[1], parts[2], int(parts[3])
            accounts[name1] = accounts.get(name1, 0) - sum_
            accounts[name2] = accounts.get(name2, 0) + sum_

        elif command == "INCOME":
            p = int(parts[1])
            for name in accounts:
                if accounts[name] > 0:
                    accounts[name] += accounts[name] * p // 100

print(" Готово! Створено файли input2.txt та output2.txt")
