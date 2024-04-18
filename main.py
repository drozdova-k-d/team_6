import csv

class Table:
  def __init__(self, src: list|str):
    # базовый атрибут
    self.data = []
    
    # загрузка,если разные источнки данных 
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
table = Table(["a", "b"])
fLine = {"a":2, "b":4}
sLine = {"a":3, "b":9}
table.add_row(fLine)
table.add_row(sLine)
print(table)

table_from_file = Table('table.csv')
print(table_from_file)
