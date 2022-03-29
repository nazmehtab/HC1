from abc import ABCMeta, abstractmethod

class Book(metaclass = ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(self):
        pass

class MyBook(Book):
    def __init__(self, title, author, price ):
        Book.__init__(self, title, author)
        self.price = price
    def display(self):
        print(f'Title: {self.title}')
        print('Author: ' + self.author)
        print(f'Price: {self.price}')

class Solution:
    if __name__ == '__main__':
        title = input()
        author = input()
        price = int(input())
        b = MyBook(title, author, price)
        b.display()


