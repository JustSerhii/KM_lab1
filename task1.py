import math as m
import matplotlib.pyplot as plt
import matplotlib as mpl

# Функція, яку ми інтегруємо
def f(x):
    return -m.log(abs(m.cos(x)))

# Метод Сімпсона для чисельного обчислення інтегралу
def simpson_method(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    i = 1

    while i < n:
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
        i += 1
    integral *= h / 3

    return integral

# Функція для підрахунку значущих цифр та похибки
def count_significant_digits(value, target_error = 0.0005):
    if value == 0:
        return 0, 0

    int_part_digits = len(str(int(abs(value))))

    if int_part_digits >= 4 or value >= target_error * 2000:
        return int_part_digits, 0.5 * 10 ** (int_part_digits - 4)

    if value < target_error:
        return 0, target_error

    error = target_error
    digits = int_part_digits
    while error > value * 0.1 and digits < 4:
        error *= 0.1
        digits += 1

    return digits, error

# Функція для створення графіку
def plot_error_graph(error_table):
    x_values = [x for x, _, _, _ in error_table]
    y_values = [y for _, y, _, _ in error_table]

    mpl.use('TkAgg')
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='g')
    plt.title("Modified Lobachevsky's Function")
    plt.xlabel('$x$')
    plt.ylabel('$F(x)$')
    plt.grid(True)
    plt.xticks(x_values, rotation=50)
    plt.tight_layout()

    for x, y, digits, error in error_table:
        plt.text(x, y, f"{y:.{digits}f}±{error:.1e}", fontsize=9, ha='right', va='bottom')

    plt.show()

# Головна функція
def main():
    step = m.pi / 36
    end = m.pi / 2

    results = []
    cumulative_integral = 0
    x = 0

    while x <= end:
        integral = simpson_method(f, x, x + step, 4)

        cumulative_integral += integral
        results.append((x, cumulative_integral))
        x += step

    error_table = []
    for x, value in results:
        digits, error = count_significant_digits(value)
        error_table.append((x, value, digits, error))

    print(error_table)

    plot_error_graph(error_table)

if __name__ == "__main__":
    main()