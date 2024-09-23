def add_everything_up(a, b):
    a = float(a)
    b = float(b)
    if a % 10 == 0:
        a = int(a)
    if b % 10 == 0:
        b = int(b)

    return a + b


first = input('Введите первый элемент: ')
second = input('Введите второй элемент: ')
try:
    print(add_everything_up(first, second))
except (TypeError, ValueError):
    print(first + second)
