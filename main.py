# необходимый пакет 
import csv

# TODO - залить на репозиторий github

class Table:
  # TODO поправить метод __init__:
  # - либо использовать параметры по умолчанию;
  # - либо обязать пользвателя вводить параметр.

  # TODO нужно чтобы класс Table принимал файлы csv
  # например, файл table.csv

  def __init__(self, columns):
    # if isinstance(obj, list) == True:
    #     pass
    # elif isinstance(obj, str) == True:

    # else:
    #     pass

    # match obj:
    #   case list():
    #       pass

    #   case str():
    #       with open(path) as table:
    #           pass


    self.columns = columns
    file_name = input("Введите имя файла csv (например, table.csv):")
    self.data = read_csv(file_name)

  def add_row(self, row) -> None:
    # TODO - добавить проверку на наличие названия колонки! +
    if not all(col in self.columns for col in row.keys()):
      raise Exception("Некорректные названия колонок")
    else:
      self.data.append(row)

  def __bool__(self) -> bool:
    return len(self.data) > 0

  def __str__(self):
    Table_str = "" 
    # Преобразование данных таблицы в строку
    Table_str += " ".join(self.columns) + "\n"
    for row in self.data:
      Table_str += " ".join(str(row[col]) for col in self.columns) + "\n"
    return Table_str

# Создание таблицы с заданными колонками
# table = Table(["a", "b"])
# fLine = {"a":2, "b":4}
# sLine = {"a":3, "b":9}
# table.add_row(fLine)
# table.add_row(sLine)
# print(table)

# # Пример с ошибкой
# errorLine = {"c":4, "b":10}
# table.add_row(errorLine)
# print (table)
def __init__(self):
    self.data = []

def add_row(self, row):
    self.data.append(row)

def print_table(self):
    if self.data:
        for row in self.data:
            print(row)
    else:
        print("Таблица пуста")

# Пустая таблица
# ошибка
# TypeError: Table.__init__() missing 1 required positional argument: 'columns'

empty_table = Table()

if empty_table:
  print("Таблица не пустая")
else:
  print("Таблица пустая")
