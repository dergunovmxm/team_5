'''
Основные принципы ООП

1. Класс — шаблон для создания объектов (экземпляров).
2. Объект — экземпляр класса с конкретными значениями.
3. Инкапсуляция — скрытие внутренней реализации объекта, доступ к данным через методы.
4. Наследование — создание новых классов на основе уже существующих.
5. Полиморфизм — возможность использовать объекты разных классов через одинаковый интерфейс.

'''

'''
-Library
-Book
-User
'''

from book import Book
from user import Student, Teacher
from library import Library

book1 = Book("Clean code", "Martin", 2017)
book2 = Book("Test", "Testov", 2019)

student = Student('Vasya')
teacher = Teacher('MariaIvanovna')

lib = Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(Book('testovaya kniga', 'Testovyi avtor' ,2009))
lib.add_book(Book('Rap god', 'Eminem', 2002))
lib.add_book(Book('Harry Potter', 'Rowling', 2000))
lib.rent_book('Clean code', student)
lib.rent_book('testovaya kniga', student)
lib.rent_book('Rap god', student)
lib.rent_book('Harry Potter', student)
lib.return_book('Clean code', student)

lib.show_books()
lib.show_browsed_book()

student.show_books()
lib.return_book('testovaya kniga', student)
student.show_books()
teacher.show_books()

