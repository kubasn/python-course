class TooManyPagesReadException(ValueError):
    pass


def devide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    
    return dividend/divisor



grades = []


try:
    print(devide(sum(grades),len(grades)))
except ZeroDivisionError:
    print('There are no grades yet in your list.')






class Book:
    def __init__(self,name:str,page_count:int):
        self.name =name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self):
        return f'<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>'

    def read(self,pages):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadException(f'you tried to read too may pages')


        self.pages_read += pages
        print( f'You have read {self.pages_read} pages out of {self.page_count}>')

book = Book('Harry Potter',250)

book.read(300)





