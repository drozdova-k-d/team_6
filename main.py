import csv

class Table:
  def __init__(self, src: list|str):
    # базовый атрибут
    self.data = []
    
    # загрузка, если разные источнки данных 
    if isinstance(src, list) == True:
        self.columns = src
      
    elif isinstance(src, str) == True: 
      with open(src, mode='r') as file:
          csv_reader = tuple(csv.DictReader(file))
          self.columns = csv_reader[0].keys()
          for row in csv_reader:
              self.data.append(row)
    else:
      raise TypeError("Таблица пустая")
      
    

    self.columns = columns
    file_name = input("Введите имя файла csv (например, table.csv):")
    self.data = read_csv(file_name)

  def add_row(self, row) -> None:
    if not all(col in self.columns for col in row.keys()):
      raise Exception("Некорректные названия колонок")
    else:
      self.data.append(row)

  def __bool__(self) -> bool:
    return len(self.data) > 0

  def __str__(self):
    Table_str = "" 
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


empty_table = Table()

if empty_table:
  print("Таблица не пустая")
else:
  print("Таблица пустая")
