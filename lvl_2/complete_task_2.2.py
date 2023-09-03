# Задача 2.2.

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например:
# месяц 2 (февраль) является частью первого квартала;
# месяц 6 (июнь) является частью второго квартала;
# месяц 11 (ноябрь) является частью четвертого квартала.

months = [
    ["январь", 1],
    ["февраль", 1],
    ["март", 1],
    ["апрель", 2],
    ["май", 2],
    ["июнь", 2],
    ["июль", 3],
    ["август", 3],
    ["сентябрь", 3],
    ["октябрь", 4],
    ["ноябрь", 4],
    ["декабрь", 4],
]


def quarter_of(month):
    return months[month - 1][1]


input_month = 11
quarter = quarter_of(input_month)
if quarter == 1:
    print('месяц', input_month, '(' + months[input_month - 1][0] + ') является частью первого квартала.')
elif quarter == 2:
    print('месяц', input_month, '(' + months[input_month - 1][0] + ') является частью второго квартала.')
elif quarter == 3:
    print('месяц', input_month, '(' + months[input_month - 1][0] + ') является частью третьего квартала.')
elif quarter == 4:
    print('месяц', input_month, '(' + months[input_month - 1][0] + ') является частью четвертого квартала.')
