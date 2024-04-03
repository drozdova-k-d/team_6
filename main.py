class Table:
  def __init__(self, columns):
    self.columns = columns
    self.data = []

  def add_row(self, row):
    # TODO - добавить проверку на наличие названия колонки!
    self.data.append(row)

  def __bool__(self):
    return len(self.data) > 0
    
  def __str__(self):
    table_str = " " 
    #Преобразование данных таблицы в строку
    table_str += " ".join(self.columns) + "\n"
    for row in self.data:
    
        row_str = "".join([str(col]) for col in self.columns])
        table_str += row_str + "\n"
    return table_str

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