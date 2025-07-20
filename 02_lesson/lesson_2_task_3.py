import math

def square(side):
    return math.ceil(side * side)

side = float(input("Сторона квардрата: "))
print(f"Площадь квадрата: {(square(side))}")
