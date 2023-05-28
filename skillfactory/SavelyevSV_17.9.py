def puz(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

text = input('Введите последовательность чисел: ')
array = list(map(int, text.split()))

array = puz(array)
print(array)

element = int(input('Индекс какого числа выводим?: '))

if element not in array:
     print(f'Нет числа {element} в последовательности. {array}')
     if element < min(array):
           print(f'Число {element} меньше минимального. {min(array)}')
     if element > max(array):
           print(f'Число {element} больше максимального. {max(array)}')
     exit(1)

index = binary_search(array, element, 0, len(array)-1)
print('Индекс числа: ',index)

if index == 0:
    print(f'Число {element} первое значение в списке, следующее {array[index + 1]}')
elif index == int(len(array)-1):
    print(f'Число {element} последнее значение в списке, предыдущее значение {array[index-1]}')
else:
    print(f'Предыдущее число {array[index-1]}, следующее число {array[index + 1]}')