friends = []

def add_friend():
    friends.append('Rolf')


add_friend()
add_friend()
add_friend()

print(friends)


tab = []
def add(x,y):
    tab.append(x+y)
    print(tab)

add(5,4)
add(5,12)
add(5,44)


def add(x,y=10):
    print(x+y)

add(5)


# return value

def divide(divided,divisor):
    if divisor != 0:
        return divided /divisor
    elif divisor == 0:
        return "Don't divide by zero"

result = divide(15,3)
print(result)

