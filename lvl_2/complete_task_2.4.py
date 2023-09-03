# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание!
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:
    rows = 0
    columns = 0
    values = []

    def add_row(self, count=1):
        self.rows += count
        for i in range(self.columns * count):
            self.values.append(1)

    def add_column(self, count=1):
        self.columns += count
        for i in range(self.rows * count):
            self.values.append(1)

    def print(self):
        values = self.values
        values.reverse()
        print("Матрица", self.rows, "x", self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                print(values.pop(), end=", ")
            print("", end="\n")


matrix = Matrix()

matrix.add_row(5)
matrix.add_column(5)

matrix.print()
