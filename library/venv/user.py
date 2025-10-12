class User:
  max_books = 3
  _user_id =  1

  def __init__(self, name):
    self.name = name
    self.borrowed_books = []
    self.id = User._user_id
    User._user_id += 1
  
  def show_books(self):
    print(f'Книги у {self.name}')
    if not self.borrowed_books:
      print('Нет взятых книг')
    for book in self.borrowed_books:
      print('- ', book)

class Student(User): 
  max_books = 3
  def __init__(self, name):
    super().__init__(name)

class Teacher(User):
  max_books = 10
  def __init__(self, name):
    super().__init__(name)

