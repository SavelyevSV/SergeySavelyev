people = int(input('Сколько билетов хотите приобрести: '))
i = 1
summa = 0
while i <= people:
    print('Введите возраст посетителя ', i)
    age = int(input())
    if 1 <= age < 18:
        print('Вход бесплатный!')
        i += 1
    elif 18 <= age < 25:
        print('Цена билета 990р' )
        summa = summa + 990
        i += 1
    elif 25 <= age <= 100:
        print('Цена билета 1390р')
        summa = summa + 1390
        i += 1
    else:
        print('Некорректный возраст')

if people >= 3:
    print('Сумма к оплате с учетом скидки 10% : ', summa*0.9)
else:
    print('Сумма к оплате: ', summa)