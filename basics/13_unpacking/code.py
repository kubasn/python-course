def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *=arg
    return total


print(multiply(1,2,4))

# named arguments

nums = {'x':5,'y':4}

def multiply1(x,y):
    return x*y


print(multiply1(**nums))




def multiply2(args):
    print(args)
    total =1
    for arg in args:
        total *= arg

    return total

def add2(args):
    total =0
    for arg in args:
        total += arg
        
    return total


# *args - collection of all arguments, operator - named argument

def apply(*args,operator):
    if operator == '*':
        return multiply2(args)
    elif operator == '+':
        return add2(args)
    else:
        return 'no valid operator'


print(apply(1,2,3,operator='+'))

########################################################################

def named(name, age):
    print(name, age)



details = {"name": "Bob", "age": 25}

named(**details)



def named1(**name):
    print(name)

def print_names(**kwargs):
    print('print names')
    for key,value in kwargs.items():
        print(f'{key} is {value}')




details = {"name": "Bob", "age": 25}

named1(name="bob",age=25)

print_names(name="bob",age=25)






def complex(*args,**kwargs):
    print(args)
    print(kwargs)

complex(4,3,2,name='Tom',age='54')
