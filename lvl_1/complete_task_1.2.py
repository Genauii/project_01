# Задача 1.2.

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
duration = my_favorite_songs[2][1] + my_favorite_songs[5][1] + my_favorite_songs[6][1]
print('Три песни звучат ' + str(duration) + ' минут')

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
duration = my_favorite_songs_dict['Waste a Moment']
duration = duration + my_favorite_songs_dict['Beautiful Day']
duration = duration + my_favorite_songs_dict['In This World']
print('Три песни звучат ' + str(duration) + ' минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
import random

duration = my_favorite_songs[random.randint(0, 8)][1]
duration = duration + my_favorite_songs[random.randint(0, 8)][1]
duration = duration + my_favorite_songs[random.randint(0, 8)][1]
print('Три песни звучат ' + str(duration) + ' минут')

my_favorite_songs_dict_keys = list(my_favorite_songs_dict.keys())
duration = my_favorite_songs_dict[random.choice(my_favorite_songs_dict_keys)]
duration = duration + my_favorite_songs_dict[random.choice(my_favorite_songs_dict_keys)]
duration = duration + my_favorite_songs_dict[random.choice(my_favorite_songs_dict_keys)]
print('Три песни звучат ' + str(duration) + ' минут')

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
from datetime import timedelta

print(timedelta(minutes=duration))
