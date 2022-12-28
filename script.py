per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('СУММА ВАШЕГО ВКЛАДА = '))
deposit = []
deposit.append(round(money*per_cent['ТКБ']/100,2))
deposit.append(round(money*per_cent['СКБ']/100,2))
deposit.append(round(money*per_cent['ВТБ']/100,2))
deposit.append(round(money*per_cent['СБЕР']/100,2))
print(deposit)
print('Максимальная сумма процентов', max(deposit))
s = list(per_cent.keys())






