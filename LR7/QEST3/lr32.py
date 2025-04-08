def process_python_code(input_filename, output_filename):
    with open(input_filename, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    inside_class = False
    updated_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("class "):
            inside_class = True

        # Якщо вийшли з класу (порожній рядок або відступи менші)
        if inside_class and not line.startswith(" ") and not stripped.startswith("class "):
            inside_class = False

        # Замінюємо "public" на "private" лише всередині класу
        if inside_class and "public" in line:
            line = line.replace("public", "private")

        updated_lines.append(line)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.writelines(updated_lines)

# Тестування: створимо тестовий файл і обробимо його
with open("test_input.py", "w", encoding="utf-8") as f:
    f.write("""\
class MyClass:
    public_var = 10
    def public_method(self):
        print("This is public")

def unrelated_function():
    public = "This should not change"
""")

# Виклик функції
process_python_code("test_input.py", "test_output.py")

print("Готово. Зміни збережено у файлі test_output.py.")
