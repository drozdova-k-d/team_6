class Table:
  def __init__(self, columns):
    self.columns = columns
    self.data = []

  def add_row(self, row):
    # TODO - добавить проверку на наличие названия колонки!
    if not all(col in self.columns for col in row.keys()):
      print ("Некорректные названия колонок")
      return
    self.data.append(row)

  def __bool__(self):
    return len(self.data) > 0
    
  def __str__(self):
    Table_str = " " 
    #Преобразование данных таблицы в строку
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

print (table)

if table:
  print("Таблица не пустая")
else:
  print("Таблица пустая")