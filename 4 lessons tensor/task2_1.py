# Напишите функцию which_triangle(a, b, c),
# На вход поступают длины трёх сторон треугольника: a, b, c
# Программа выводит какой это треугольник type_triangle: "Равносторонний", "Равнобедренный", "Обычный".
# Либо "Не треугольник", если по переданным параметрам невозможно построить треугольник
# Например 1, 1, 1 --> "Равносторонний"

def which_triangle(a, b, c):
    # Здесь нужно написать код
    if a == b == c != 0:
        type_triangle = 'Равносторонний'
        return type_triangle
    elif (a == b != 0 or a == c != 0 or b == c != 0) and (a + b > c and a + c > b and b + c > a):
        type_triangle = 'Равнобедренный'
        return type_triangle
    elif a != b and a != c and b != c and a + b > c and a + c > b and b + c > a:
        type_triangle = 'Обычный'
        return type_triangle
    elif a + b <= c or a + c <= b or b + c <= a:
        type_triangle = 'Не треугольник'
        return type_triangle


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3),
    (1, 1, 6)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник", "Не треугольник"
]


for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
