# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите номер месяца, когда поедете в отпуск: '))
month_list = ['winter','winter','spring','spring','spring','summer','summer','summer','autumn','autumn','autumn','winter']
month_dict = { 1: 'winter', 2: 'winter', 12: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn',10: 'autumn',11: 'autumn'}
if month in month_dict:
    print('Время года по списку: ', month_list[month-1])
    print('Время года по словарю: ', month_dict.get(month))
else:
    print('Нет такого месяца!')