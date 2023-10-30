import math

def f(x: float) -> float:
    if x == 0:
        return 0
    return 1 / (math.sqrt(x**3 + x))

def trapezoid_integration(a, b, h):
    I = 0
    while a < b:
        I += (f(a) + f(a + h)) * h / 2
        a += h
    return I

# Параметри для обчислень
a_1, b_1 = 0, 1/64
h_1 = 1/64**2

a_2, b_2 = 1/64, 1
h_2 = (b_2 - a_2) / 1000

# Інтеграція з кроком h і h/2
I1_h = trapezoid_integration(a_1, b_1, h_1)
I1_h2 = trapezoid_integration(a_1, b_1, h_1/2)

# Правило Рунге для інтегралу від 0 до 1/64
p = 2
R1 = abs(I1_h2 - I1_h) / (2**p - 1)

# Отримана точність для інтегралу від 1/64 до 1
accuracy = 0.5
R2_allowed = accuracy - R1

# Обчислення інтегралу від 1/64 до 1 з потрібною точністю
I2_h = trapezoid_integration(a_2, b_2, h_2)
I2_h2 = trapezoid_integration(a_2, b_2, h_2/2)
R2 = abs(I2_h2 - I2_h) / (2**p - 1)

print(f"Результат I(h1) від 0 до 1/64 = {I1_h}")
print(f"Похибка Рунге для інтегралу від 0 до 1/64: {R1}")
print(f"Дозволена похибка для інтегралу від 1/64 до 1: {R2_allowed}")
print(f"Похибка Рунге для інтегралу від 1/64 до 1: {R2}")
print(f"Результат I(h2) від 1/64 до 1 = {I2_h}")
print(f"Загальний результат I від 0 до 1 = {I1_h + I2_h}")
