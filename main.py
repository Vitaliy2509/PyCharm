per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('СУММА ВАШЕГО ВКЛАДА = '))
deposit = []
deposit.append(round(money*per_cent['ТКБ']/100,2))
deposit.append(round(money*per_cent['СКБ']/100,2))
deposit.append(round(money*per_cent['ВТБ']/100,2))
deposit.append(round(money*per_cent['СБЕР']/100,2))
print('Депозит =', deposit)
s = list(per_cent.keys())
d = dict(zip(s, deposit))
print('Варианты по доходности за год по банкам:', d)
print('Максимальная сумма процентов:', max(deposit))


