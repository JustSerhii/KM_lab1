import numpy as np
from math import sqrt, exp, pi

# Функція, яку потрібно інтегрувати
def f(x):
    return 1 / exp(x**2 - x)

# Значення нулів полінома Ерміта
x1 = 0
x2 = sqrt(3/2)
x3 = -sqrt(3/2)

# Коефіцієнти c_k
c1 = 1.1816
c2 = 0.2954
c3 = 0.2954

# Обчислення інтеграла
I = c1 * f(x1) + c2 * f(x2) + c3 * f(x3)

from scipy.integrate import quad
analytical_value, _ = quad(f, -10, 10)  # Обмежуємо діапазон для оцінки похибки

print("Значення інтеграла I:", I)
print("Аналітичне значення інтеграла:", analytical_value)
print("Похибка:", abs(I - analytical_value))