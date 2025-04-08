def calculator():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        op = input("Введіть операцію (+, -, *, /, mod, pow, div): ")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        elif op == "mod":
            result = a % b
        elif op == "pow":
            result = a ** b
        elif op == "div":
            result = a // b
        else:
            print("Невідома операція!")
            return
    except ZeroDivisionError:
        print("Division by zero!")
    except ValueError:
        print("Помилка: потрібно ввести числа.")
    else:
        print("Результат:", result)
    finally:
        print("Роботу завершено.")

# Запуск
calculator()
