class Book:
  _id = 1

  def __init__(self, title, author, year):

    self.id = Book._id
    Book._id += 1

    self._title = title
    self._author = author
    self._year = year

  @property
  def title(self):
    return self._title
  
  @property
  def author(self):
    return self._author
  
  @property
  def year(self):
    return self._year
  
  @title.setter
  def set_title(self, value):
    self._title = value

  @author.setter
  def set_author(self, value):
      self._author = value

  @year.setter
  def set_year(self, value):
    self._year = value

  def __str__(self):
    return f"[ID: {self.id}] '{self.title}' автор  {self.author} год ({self.year}) "
