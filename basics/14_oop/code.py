class Student:
    def __init__(self,name,grades): #constructor self-this
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades)/len(self.grades)

# is called when you wan't to turn your object to string like print(rolf)
    def __str__(self):
        return f'Student name: {self.name}, grades:{self.grades}'
    
    def __repr__(self):
        return f"<Person('{self.name}',{self.grades})>"
    
    @classmethod
    def class_method(cls):
        print(f'called class_method of {cls}')

    @staticmethod
    def static_method():
        print('Called static_method')



rolf = Student('Rolf',(20,40,50))

print(rolf)
print(rolf.average())

print(rolf.__repr__())

# class method can acess and modify the class state
# static method cannot access or modify the class state

# static method - seperate function that lives inside class, that you put there
# if you fill it should belongs there
# class method used as foctories


class Book:
    TYPES = ('hardcover','paperback')


    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, weighting {self.weight}g>'

    @classmethod
    def hardcover(cls,name,page_weight):
        return Book(name,Book.TYPES[0],page_weight+100)

    @classmethod
    def lightcover(cls,name,page_weight):
        return Book(name,Book.TYPES[1],page_weight+10)

book = Book.hardcover('Harry Potter',1500)

print(book)



class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        name = store.name + ' - franchise'
        return cls(name)


    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        total = 0

        return f'{store.name}, total stock price: {int(store.stock_price())}'
