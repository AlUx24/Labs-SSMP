test_cases = [6785, 456789, 86401]

for total_seconds in test_cases:
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s).")

# Вхідні дані:
# 6785
# 456789
# 86401

# Вихідні дані:
# 0 day(s), 1 hour(s), 53 minute(s), 5 second(s).
# 5 day(s), 6 hour(s), 53 minute(s), 9 second(s).
# 1 day(s), 0 hour(s), 0 minute(s), 1 second(s).
