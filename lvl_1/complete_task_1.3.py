# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца,
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

months = [
    ["январь", 31],
    ["февраль", 28],
    ["март", 31],
    ["апрель", 30],
    ["май", 31],
    ["июнь", 30],
    ["июль", 31],
    ["август", 31],
    ["сентябрь", 30],
    ["октябрь", 31],
    ["ноябрь", 30],
    ["декабрь", 31],
]

month = int(input("Введите номер месяца: "))
if month > 12:
    print("Такого месяца нет!")
else:
    print("Вы ввели " + months[month - 1][0] + ". " + str(months[month - 1][1]) + " дней")
