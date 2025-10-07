class Library:
  def __init__(self):
    self.books = [] 
    self.borrowed_books = {} #{ book: user }

  def add_book(self, book):
    self.books.append(book)

  def show_books(self):
    print('Все книги в библиотеке')
    for book in self.books:
      print("* ", book)
  
  def show_browsed_book(self):
    print('Выданные книги')
    for book, user in self.borrowed_books.items():
      print(f"{book} у {user.name}")

  def rent_book(self, book_title, user):
    #проверка на доступность выдачи книги
    for book in self.books:
      if book.title == book_title:
        self.books.remove(book)
        self.borrowed_books[book] = user
        user.borrowed_books.append(book)
        print(f"Книга {book_title} выдана {user.name}")
        return
    print('Такой книги нет')

  # def  return_book - вернуть книгу
  # def  is_borrowed_book - проверить на наличие книги 
  

