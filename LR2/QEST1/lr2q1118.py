for _ in range(3):
    v = float(input())
    if v < 7.8:
        print("The device fell to Earth.")
    elif 7.8 <= v < 11.2:
        print("The device became a satellite of the Earth.")
    elif 11.2 <= v < 16.4:
        print("The device became a satellite of the Sun.")
    else:
        print("The device left the Solar system.")

# Вхідні дані:
# 12.5
# 22.56
# 8.3
#
# Вихідні дані:
# The device became a satellite of the Sun.
# The device left the Solar system.
# The device became a satellite of the Earth.
