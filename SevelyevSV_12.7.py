money=int(input("Введите сумму: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [round(money*per_cent['ТКБ']/100, 2), round(money*per_cent['СКБ']/100, 2),
           round(money*per_cent['ВТБ']/100, 2), round(money*per_cent['СБЕР']/100, 2)]
print("deposit = ", deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit))