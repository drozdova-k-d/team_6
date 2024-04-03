class Table:
  def __init__(self, columns):
    self.columns = columns
    self.data = []

  def add_row(self, row):
    self.data.append(row)
      
#fLine = {"a" : 2, "b" : 4}
#sLine = {"a" : 3, "b" : 9}