from typing import List

# mutability
a = []
b = a

# prints reference to the same object
# 2594157411904
# 2594157411904
# that means they are the same object
print(id(a))
print(id(b))



# default paramter


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is bad!
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)

bob = Student('Bob')
mark = Student('Mark')

bob.take_exam(10)

print(bob.grades)  # [10]
print(mark.grades) # [10]


# The function parameters evaluate when the function is defined, not when it runs.
# That means that self.grades is a name for the list that was evaluated when the function was defined.
# We're then modifying it in take_exam
# But all calls to the __init__ method have the same list (because parameters are only evaluated once!)
# So all students have the same list


# Avoid it by not having mutable parameters.

class Student:
    def __init__(self,name,grades:List[int]=None):
        self.name =name
        self.grades = grades or [] #create new list if one isn't passed
    def take_exam(self,result):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Now it's empty.